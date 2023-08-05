# from  el_wikipedia import entity_linking

def entity_linking_wiki():
    print('Entity Linking Package via Wikipedia is installed in init!!!')


import pandas as pd
import spacy
nlp = spacy.load('en_core_web_md')

# add pipeline

import spacy_entity_linker as entityLinker

nlp.add_pipe("entityLinker", last=True)

# from flask import *
import json, time

# myapp = Flask(__name__)

def Entity_Linking_via_Wikipedia(usrip_el):
    try:
        ip_sent_lst = list(usrip_el.split('. '))
        df_sent = pd.DataFrame(ip_sent_lst)
        final_opt = pd.DataFrame()
        final_opt = Entity_Linking_via_Wiki(df_sent)
        return final_opt
        # final_json = final_opt.to_json(orient='records')
        # data_set = {'Original Input': f'{usrip_el}',
        #             'Parsing': f'{final_json}'}
        # json_data = json.dumps(data_set)
        # return json_data

    except Exception as e:
        print('Error is :', e)


def Entity_Linking_via_Wiki(df):
    # doc2 = nlp(df_sample.iloc[0][0])
    # doc2 = nlp(df_sample.to_string())
    doc2 = nlp(df.to_string())
    all_linked_entities = doc2._.linkedEntities
    #     all_linked_entities.pretty_print()
    return wiki_linking(all_linked_entities)


def wiki_linking(linked_ent):
    df_ner_wiki_linking = pd.DataFrame(columns=['Entity','Wiki Desc', 'Wiki Link'])
    index = 0
    for index in range(len(linked_ent)):
        entity = linked_ent[index].get_label()
        wiki_desc = linked_ent[index].get_description()
        wiki_link = linked_ent[index].get_url()
        new_row = {'Entity':entity,'Wiki Desc':wiki_desc, 'Wiki Link':wiki_link}
        tempDf = pd.DataFrame([new_row])
        df_ner_wiki_linking = pd.concat([df_ner_wiki_linking, tempDf], ignore_index=True)
        # df_ner_wiki_linking = df_ner_wiki_linking.append(new_row, ignore_index=True)
        # df_ner_wiki_linking.append(new_row)
        df_ner_wiki_linking

    return df_ner_wiki_linking
