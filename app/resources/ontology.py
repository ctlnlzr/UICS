def get_ontology():
    return """You are a natural language - SPARQL convertor, using the following ontology:
              @prefix : <http://www.semanticweb.org/pc/ontologies/2024/0/untitled-ontology-2/> .
              @prefix owl: <http://www.w3.org/2002/07/owl#> .
              @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
              @prefix xml: <http://www.w3.org/XML/1998/namespace> .
              @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
              @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
              @prefix untitled-ontology-2: <http://www.semanticweb.org/pc/ontologies/2024/0/untitled-ontology-2#> .
              @base <http://www.semanticweb.org/pc/ontologies/2024/0/untitled-ontology-2/> .
              <http://www.semanticweb.org/pc/ontologies/2024/0/untitled-ontology-2> rdf:type owl:Ontology .
              untitled-ontology-2:contains rdf:type owl:ObjectProperty ;
                                           rdfs:domain untitled-ontology-2:Tags ;
                                           rdfs:range untitled-ontology-2:Tags .
              owl:topObjectProperty rdfs:subPropertyOf untitled-ontology-2:contains .
              untitled-ontology-2:code rdf:type owl:DatatypeProperty .
              untitled-ontology-2:Ion_Card rdf:type owl:Class ;
                                           rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Card_Content rdf:type owl:Class ;
                                                   rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Card_Header rdf:type owl:Class ;
                                                  rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Card_Subtitle rdf:type owl:Class ;
                                                    rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Card_Title rdf:type owl:Class ;
                                                 rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Col rdf:type owl:Class ;
                                          rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Content rdf:type owl:Class ;
                                              rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Element rdf:type owl:Class ;
                                              rdfs:subClassOf untitled-ontology-2:Tags .
              untitled-ontology-2:Ion_Footer rdf:type owl:Class ;
                                             rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Grid rdf:type owl:Class ;
                                           rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Header rdf:type owl:Class ;
                                             rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Img rdf:type owl:Class ;
                                          rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Input rdf:type owl:Class ;
                                            rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Item rdf:type owl:Class ;
                                           rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_List rdf:type owl:Class ;
                                           rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Row rdf:type owl:Class ;
                                          rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Ion_Title rdf:type owl:Class ;
                                            rdfs:subClassOf untitled-ontology-2:Ion_Element .
              untitled-ontology-2:Paragraph rdf:type owl:Class ;
                                            rdfs:subClassOf untitled-ontology-2:Regular_Elements .
              untitled-ontology-2:Regular_Elements rdf:type owl:Class ;
                                                   rdfs:subClassOf untitled-ontology-2:Tags .
              untitled-ontology-2:Tags rdf:type owl:Class .
              untitled-ontology-2:CardContent_1 rdf:type owl:NamedIndividual ,
                                              untitled-ontology-2:Ion_Card_Content ;
                                     untitled-ontology-2:contains untitled-ontology-2:Paragraph ;
              untitled-ontology-2:CardContent_2 rdf:type owl:NamedIndividual ,
                                                           untitled-ontology-2:Ion_Card_Content ;
                                                  untitled-ontology-2:contains untitled-ontology-2:Image ,
                                                                               untitled-ontology-2:Input ;
              untitled-ontology-2:CardHeader_1 rdf:type owl:NamedIndividual ,
                                                      untitled-ontology-2:Ion_Card_Header ;
                                             untitled-ontology-2:contains untitled-ontology-2:CardSubtitle ,
                                                                          untitled-ontology-2:CardTitle ;
              untitled-ontology-2:CardHeader_2 rdf:type owl:NamedIndividual ,
                                                          untitled-ontology-2:Ion_Card_Header ;
                                                 untitled-ontology-2:contains untitled-ontology-2:CardTitle ;
              untitled-ontology-2:CardSubtitle rdf:type owl:NamedIndividual ,
                                                          untitled-ontology-2:Ion_Card_Subtitle ;               
              untitled-ontology-2:CardTitle rdf:type owl:NamedIndividual ,
                                                       untitled-ontology-2:Ion_Card_Title ;
              untitled-ontology-2:Card_1 rdf:type owl:NamedIndividual ,
                                                    untitled-ontology-2:Ion_Card ;
                                           untitled-ontology-2:contains untitled-ontology-2:CardContent_1 ,
                                                                        untitled-ontology-2:CardHeader_1 ;
              untitled-ontology-2:Card_2 rdf:type owl:NamedIndividual ,
                                                    untitled-ontology-2:Ion_Card ;
                                           untitled-ontology-2:contains untitled-ontology-2:CardContent_2 ,
                                                                        untitled-ontology-2:CardHeader_2 ;
              untitled-ontology-2:Column_1 rdf:type owl:NamedIndividual ,
                                                      untitled-ontology-2:Ion_Col ;
              untitled-ontology-2:Column_2 rdf:type owl:NamedIndividual ,
                                                      untitled-ontology-2:Ion_Col ;
              untitled-ontology-2:Column_3 rdf:type owl:NamedIndividual ,
                                                      untitled-ontology-2:Ion_Col ;
              untitled-ontology-2:Column_4 rdf:type owl:NamedIndividual ,
                                                      untitled-ontology-2:Ion_Col ;
              untitled-ontology-2:Footer_1 rdf:type owl:NamedIndividual ,
                                                      untitled-ontology-2:Ion_Footer ;
                                             untitled-ontology-2:contains untitled-ontology-2:Title_1 ;
              untitled-ontology-2:Grid_1 rdf:type owl:NamedIndividual ,
                                                    untitled-ontology-2:Ion_Grid ;
                                           untitled-ontology-2:contains untitled-ontology-2:Row_1 ,
                                                                        untitled-ontology-2:Row_2 ,
                                                                        untitled-ontology-2:Row_3 ;
              untitled-ontology-2:Image rdf:type owl:NamedIndividual ,
                                                   untitled-ontology-2:Ion_Img ;
              untitled-ontology-2:Input rdf:type owl:NamedIndividual ,
                                                   untitled-ontology-2:Ion_Input ;
              untitled-ontology-2:ListItem_1 rdf:type owl:NamedIndividual ,
                                                        untitled-ontology-2:Ion_Item ;
                                               untitled-ontology-2:contains untitled-ontology-2:Paragraph ;
              untitled-ontology-2:ListItem_2 rdf:type owl:NamedIndividual ,
                                                        untitled-ontology-2:Ion_Item ;
                                               untitled-ontology-2:contains untitled-ontology-2:Paragraph ;
              untitled-ontology-2:ListItem_3 rdf:type owl:NamedIndividual ,
                                                        untitled-ontology-2:Ion_Item ;
                                               untitled-ontology-2:contains untitled-ontology-2:Paragraph ;
              untitled-ontology-2:List_1 rdf:type owl:NamedIndividual ,
                                                    untitled-ontology-2:Ion_List ;
                                           untitled-ontology-2:contains untitled-ontology-2:ListItem_1 ,
                                                                        untitled-ontology-2:ListItem_2 ,
                                                                        untitled-ontology-2:ListItem_3 ;
              untitled-ontology-2:PageContent_1 rdf:type owl:NamedIndividual ,
                                                           untitled-ontology-2:Ion_Content ;
                                                  untitled-ontology-2:contains untitled-ontology-2:Grid_1 ,
                                                                               untitled-ontology-2:Paragraph ;
              untitled-ontology-2:PageContent_2 rdf:type owl:NamedIndividual ,
                                                           untitled-ontology-2:Ion_Content ;
                                                  untitled-ontology-2:contains untitled-ontology-2:Image ,
                                                                               untitled-ontology-2:List_1 ;
              untitled-ontology-2:PageHeader_1 rdf:type owl:NamedIndividual ,
                                                          untitled-ontology-2:Ion_Header ;
                                                 untitled-ontology-2:contains untitled-ontology-2:Title_1 ;                                                                                
              untitled-ontology-2:Paragraph rdf:type owl:NamedIndividual ,
                                                       untitled-ontology-2:Paragraph ;
              untitled-ontology-2:Row_1 rdf:type owl:NamedIndividual ,
                                                   untitled-ontology-2:Ion_Row ;
                                          untitled-ontology-2:contains untitled-ontology-2:Column_1 ,
                                                                       untitled-ontology-2:Column_2 ,
                                                                       untitled-ontology-2:Column_3 ,
                                                                       untitled-ontology-2:Column_4 ;                              
              untitled-ontology-2:Row_2 rdf:type owl:NamedIndividual ,
                                                   untitled-ontology-2:Ion_Row ;
                                          untitled-ontology-2:contains untitled-ontology-2:Column_1 ,
                                                                       untitled-ontology-2:Column_2 ,
                                                                       untitled-ontology-2:Column_3 ,
                                                                       untitled-ontology-2:Column_4 ;
              untitled-ontology-2:Row_3 rdf:type owl:NamedIndividual ,
                                                   untitled-ontology-2:Ion_Row ;
                                          untitled-ontology-2:contains untitled-ontology-2:Column_1 ,
                                                                       untitled-ontology-2:Column_2 ,
                                                                       untitled-ontology-2:Column_3 ,
                                                                       untitled-ontology-2:Column_4 ;
              untitled-ontology-2:Title_1 rdf:type owl:NamedIndividual ,
                                                     untitled-ontology-2:Ion_Title ;"""


def get_training_answer():
    return """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
              PREFIX untitled-ontology-2: <http://www.semanticweb.org/pc/ontologies/2024/0/untitled-ontology-2#>
              SELECT ?code
              WHERE {
                ?cardContent rdf:type untitled-ontology-2:Ion_Card_Content.
                ?cardContent untitled-ontology-2:contains ?img, ?input.
                ?img rdf:type untitled-ontology-2:Ion_Img.
                ?input rdf:type untitled-ontology-2:Ion_Input.
                ?cardContent untitled-ontology-2:code ?code.
              }"""


def get_training_question():
    return "Convert the following description in a SPARQL query: Create a template for the card content including an" \
           " image and an ion-input. Please return only the code data property"


def get_question(description):
    return "Convert the following description in a SPARQL query: {}. Please return only the code data property"\
        .format(description)
