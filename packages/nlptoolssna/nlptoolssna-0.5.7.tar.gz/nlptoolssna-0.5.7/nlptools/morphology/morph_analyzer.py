import pickle
from nlptools.morphology import settings 
import re
from nlptools.morphology.tokenizers_words import simple_word_tokenize
from nlptools.parse.parser import arStrip
import os.path
from nlptools.DataDownload import downloader
from nlptools.morphology.charsets import AR_CHARSET, AR_DIAC_CHARSET
import copy
# def load_ALMA_dic():
#    # Open the Pickle file in binary mode
#     filename = 'ALMA27012000.pickle'
#     path =downloader.get_appdatadir()
#     file_path = os.path.join(path, filename)
    

#     with open(file_path, 'rb') as f:
#        #Load the serialized data from the file
#        ALMA_dic = pickle.load(f)
#        #print(ALMA_dic)
#        return ALMA_dic
_IS_AR_RE = re.compile(u'^[' + re.escape(u''.join(AR_CHARSET)) + u']+$')
def find_solution(token, language, task):
    """
    Given a token, this method finds the morphological solution lemma and/or pos based on a spesific language and task.
          
    Args:
        - token (:obj:`str`): The Arabic token to be morphologcaly analyzed.
        - language (:obj:`str`): In the current version, `MSA` is only supported. 
        - task (:obj:`str`): The task to filter the results by [lemmatizer, pos, full]. The defualt task if not specified is `full`.

    Returns:
        list (:obj:`list`): A list of [token, lemma, pos], where:
            - token: the original input token
            - lemma: the lemma of the token 
            - pos: the part-of-speech of the token 
            If no sloution is found for this token, an empty list is returned.
    """
    if token in settings.div_dic.keys():
        soluation = settings.div_dic[token]
        return  [token, soluation[0], soluation[1]]               
    else:
        return []

def analyze(text, language ='MSA', task ='full'):
   """
    This method takes a text as input and returns a morphological solution for each token in this text, Based on the input language and task, such that,
    if:
         - the task is lemmatizer, then the morphological soltuion is only the lemma.
         - the task is pos, then the morphological soltuion is only the pos.
         - the task is full, the the morphological soltuion is both the lemma and the pos.
     
    Args:
        - token (:obj:`str`): The Arabic token to be morphologcaly analyzed.
        - language (:obj:`str`): In the current version, `MSA` is only supported. 
        - task (:obj:`str`): The task to filter the results by [lemmatizer, pos, full]. The defualt task if not specified is `full`.
         
    Returns:
        list (:obj:`list`): A list of [token, lemma, pos], based on the spesified task, where:
            - token: the original input token
            - lemma: the lemma of the token 
            - pos: the part-of-speech of the token 

    """
  
   #@check if the init does not load data correctly, call load_alma inside
   output_list = []

   tokens = simple_word_tokenize(text)

   for token in tokens:
         result_token =[]
         token = arStrip(token , False , True , False , False , False , False) 
         token = re.sub('[ٱ]','ﺍ',token)
         solution=[token, token+"_0",""]

         if token.isdigit():
            solution[2] = "digit" #pos

         elif not _is_ar(token):
            solution[2] = "Foreign" #pos

        #  elif re.match("^[a-zA-Z]*$", token): 
        #     solution[2] = "Foreign" #pos

         else:
            result_token = find_solution(token,language, task)
            
           
            if result_token == []:
               token_without_al = re.sub(r'^[ﻝ]','',re.sub(r'^[ﺍ]','',token))
               if len(token_without_al) > 5  :
                  result_token = find_solution(token_without_al, language, task)

            if result_token == []:
              # try with replace ﻩ with ﺓ
               result_token = find_solution(re.sub(r'[ﻩ]$','ﺓ',token), language, task)
               

            if result_token == []:
               # try with unify Alef
               word_with_unify_alef = arStrip(token , False , False , False , False , True , False) # Unify Alef
               result_token = find_solution(word_with_unify_alef, language, task)
            
            if result_token == []:
               # try with remove diac
               word_undiac = arStrip(token , True , False , True , True , False , False) # remove diacs, shaddah ,  digit
               result_token = find_solution(word_undiac, language, task)

            if result_token == []:
               # try with remove diac and unify alef
               word_undiac = arStrip(token , True , True , True , False, True , False) # diacs , smallDiacs , shaddah ,  alif
               result_token = find_solution(word_undiac, language, task)

         if result_token != []:
               
               output_list.append(result_token)
         else:
            # if no solution is found
            output_list.append(solution)
        
   return filter_results(task, output_list)


def filter_results(task, lst):
    if task == 'lemmatizer':
        return remove_items_by_index(lst, [2])
    elif task == 'pos':
        return remove_items_by_index(lst, [1])
    else: 
        return lst


def remove_items_by_index(lst, index_list):
    out_put_list= copy.deepcopy(lst)
    for inner_list in out_put_list:
        for index in sorted(index_list, reverse=True):
            if len(inner_list) > index:
                inner_list.pop(index)
    return out_put_list


def _is_ar(word):
    return _IS_AR_RE.match(word) is not None       
        
# def tagger(text: str, task = 'full', language = 'MSA'):

#     """
#     This method takes an Arabic text as input, tokenize it into tokens and calles the morphological tagger to return the morpological solution for each token in this text.
#     There is no limit for the text size, but one should be resonable based on the available resources (computational power).
    
#         Args:
#             - text (:obj:`str`): The input Arabic text to be morphologically analyzed and tagged.
#             - task (:obj:`str`): The type of morphological analysis and tagging to be performed (the default is `full`).
#             - language (:obj:`str`): The language of the input text (the default is 'MSA' (Modern Standard Arabic)).
        
#     Returns:
#            - output_list list(:obj:`list`): A list of lists, where each sublist contains information about a token in the input text, including the original token, its lemma, its part of speech (POS) tag, its lemma frequency, the task and the language.

#     **Example:**

#     .. highlight:: python
#     .. code-block:: python

#          from nlptools.morph import morph_tagger
      
#          # Return the morpological solution for each token in this text
#          morph_tagger.tagger('ذهب الولد الى المدرسة')

#          # the output
#             [['ذهب', 'فعل', 349890, 'MSA', 'lemmatizer'],
#             ['الولد', 'اسم', 320244, 'MSA', 'lemmatizer'],
#             ['الى', 'كلمة وظيفية', 20215999, 'MSA', 'lemmatizer'],
#             ['المدرسة', 'اسم', 561184, 'MSA', 'lemmatizer']]
#     """
    
#     # Check if the ALMA dictionary has been loaded
#     if settings.flag == True:
#         settings.flag = False
#         settings.div_dic = load_ALMA_dic()
   
    
#     # Perform morphological tagging for the input text
#     output_list = morph_tagger(text,language, task)
    
#     # Return a list of morphological solution for each token in the input text
#     return output_list

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
    
    
    
    
