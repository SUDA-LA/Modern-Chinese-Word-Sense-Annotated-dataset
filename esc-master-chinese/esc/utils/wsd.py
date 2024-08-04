from typing import NamedTuple, Optional, List, Callable, Tuple, Iterable
import xml.etree.cElementTree as ET
from xml.dom import minidom
import json

pos_map = {
    # U-POS
    "NOUN": "n",
    "VERB": "v",
    "ADJ": "a",
    "ADV": "r",
    "PROPN": "n",
    # PEN
    "AFX": "a",
    "JJ": "a",
    "JJR": "a",
    "JJS": "a",
    "MD": "v",
    "NN": "n",
    "NNP": "n",
    "NNPS": "n",
    "NNS": "n",
    "RB": "r",
    "RP": "r",
    "RBR": "r",
    "RBS": "r",
    "VB": "v",
    "VBD": "v",
    "VBG": "v",
    "VBN": "v",
    "VBP": "v",
    "VBZ": "v",
    "WRB": "r",
}


class AnnotatedToken(NamedTuple):
    text: str
    lemma: Optional[str] = None


class WSDInstance(NamedTuple):
    annotated_token: AnnotatedToken
    labels: Optional[List[str]]
    instance_id: Optional[str]

def read_from_chinese(
    xml_path: str,
    key_path: Optional[str] = None,
    instance_transform: Optional[Callable[[WSDInstance], WSDInstance]] = None,
) -> Iterable[List[WSDInstance]]:
    
    with open(xml_path,encoding='utf-8') as f:

        for line in f:
            line=line.strip().split()
            instance_id,sentence,word,labels,delete_labels=line[0],line[1],line[2],line[3],line[4]
            sentence=sentence.replace(word,'\n'+word+'\n',1)
            sentence=sentence.split('\n',2)
            delete_labels=delete_labels.split('$$')
            wsd_sentence=[]

            for word_instance in sentence:
                if word==word_instance:
                    annotated_token=AnnotatedToken(
                        text=word_instance,lemma=word_instance
                    )

                    wsd_instance=WSDInstance(
                        annotated_token=annotated_token,
                        labels=[labels],
                        instance_id=instance_id,
                    )
                elif word_instance=='':
                    continue
                else:
                    annotated_token=AnnotatedToken(
                        text=word_instance,lemma=word_instance
                    )

                    wsd_instance=WSDInstance(
                        annotated_token=annotated_token,
                        labels=None,
                        instance_id=None,
                    )
                wsd_sentence.append(wsd_instance)
            
            yield wsd_sentence,delete_labels

def read_from_raganato(
    xml_path: str,
    key_path: Optional[str] = None,
    instance_transform: Optional[Callable[[WSDInstance], WSDInstance]] = None,
) -> Iterable[Tuple[str, str, List[WSDInstance]]]:
    def read_by_text_iter(xml_path: str):

        it = ET.iterparse(xml_path, events=("start", "end"))
        _, root = next(it)

        for event, elem in it:
            if event == "end" and elem.tag == "text":
                document_id = elem.attrib["id"]
                for sentence in elem:
                    sentence_id = sentence.attrib["id"]
                    for word in sentence:
                        yield document_id, sentence_id, word

            root.clear()

    mapping = {}

    if key_path is not None:
        try:
            with open(key_path) as f:
                for line in f:
                    line = line.strip()
                    wsd_instance, *labels = line.split(" ")
                    mapping[wsd_instance] = labels
        except Exception:
            pass

    last_seen_document_id = None
    last_seen_sentence_id = None

    for document_id, sentence_id, element in read_by_text_iter(xml_path):

        if last_seen_sentence_id != sentence_id:

            if last_seen_sentence_id is not None:
                yield last_seen_document_id, last_seen_sentence_id, sentence

            sentence = []
            last_seen_document_id = document_id
            last_seen_sentence_id = sentence_id

        annotated_token = AnnotatedToken(
            text=element.text, pos=element.attrib.get("pos", None), lemma=element.attrib.get("lemma", None)
        )

        wsd_instance = WSDInstance(
            annotated_token=annotated_token,
            labels=None
            if element.tag == "wf" or element.attrib["id"] not in mapping
            else mapping[element.attrib["id"]],
            instance_id=None if element.tag == "wf" else element.attrib["id"],
        )

        if instance_transform is not None:
            wsd_instance = instance_transform(wsd_instance)

        sentence.append(wsd_instance)

    yield last_seen_document_id, last_seen_sentence_id, sentence


def expand_raganato_path(path: str) -> Tuple[str, str]:
    path = path.replace(".data.xml", "").replace(".gold.key.txt", "")
    return f"{path}.data.xml", f"{path}.gold.key.txt"

def expand_data_path(path: str) -> Tuple[str,str]:
    path = path.replace(".data.txt","").replace(".gold.key.txt","")
    return f"{path}.data.txt",f"{path}.gold.keyt.txt"


class RaganatoBuilder:
    def __init__(self, lang: str, source: str):
        self.corpus = ET.Element("corpus")
        self.corpus.set("lang", lang)
        self.corpus.set("source", source)
        self.current_text_section = None
        self.current_sentence_section = None
        self.gold_senses = []

    def open_text_section(self, text_id: str, text_source: str = None):
        text_section = ET.SubElement(self.corpus, "text")
        text_section.set("id", text_id)
        if text_source is not None:
            text_section.set("source", text_source)
        self.current_text_section = text_section

    def open_sentence_section(self, sentence_id: str):
        sentence_section = ET.SubElement(self.current_text_section, "sentence")
        sentence_id = self.compute_id([self.current_text_section.attrib["id"], sentence_id])
        sentence_section.set("id", sentence_id)
        self.current_sentence_section = sentence_section

    def add_annotated_token(
        self, token: str, lemma: str, pos: str, instance_id: Optional[str] = None, sense: Optional[str] = None
    ):
        if instance_id is not None and sense is not None:
            token_element = ET.SubElement(self.current_sentence_section, "instance")
            token_id = self.compute_id([self.current_sentence_section.attrib["id"], instance_id])
            token_element.set("id", token_id)
            self.gold_senses.append((token_id, sense))
        else:
            token_element = ET.SubElement(self.current_sentence_section, "wf")
        token_element.set("lemma", lemma)
        token_element.set("pos", pos)
        token_element.text = token

    @staticmethod
    def compute_id(chain_ids: List[str]) -> str:
        return ".".join(chain_ids)

    def store(self, data_output_path: str, labels_output_path: Optional[str]):
        self.__store_xml(data_output_path)
        if labels_output_path is not None:
            self.__store_labels(labels_output_path)

    def __store_xml(self, output_path: str):
        corpus_writer = ET.ElementTree(self.corpus)
        with open(output_path, "wb") as f_xml:
            corpus_writer.write(f_xml, encoding="UTF-8", xml_declaration=True)
        dom = minidom.parse(output_path)
        pretty_xml = dom.toprettyxml()
        with open(output_path, "w") as f_xml:
            f_xml.write(pretty_xml)

    def __store_labels(self, output_path: str):
        with open(output_path, "w") as f_labels:
            for gold_sense in self.gold_senses:
                f_labels.write(" ".join(gold_sense))
                f_labels.write("\n")

def cn_senses_from_dic(
    word:str,
    del_labels,
    senses_dic:str,
) -> List[str]:

    with open(senses_dic,encoding='utf-8') as f:
        dic_all=json.load(f)
        out_lst=[i for i in dic_all[word] if i not in del_labels]
        return out_lst