import os
import json
import pickle as pkl
import re

def padding(v_sentence):

    if len(v_sentence) == 18:
        v_sentence.insert(0,0)
        v_sentence.append(1)

    elif len(v_sentence) < 18:
        v_sentence.insert(0,0)
        while len(v_sentence) != 19:
            v_sentence.append(2) # insert padding
        v_sentence.append(1)

    # remove until only 20 words with start and end
    elif len(v_sentence) > 18:
        v_sentence.insert(0,0)
        while len(v_sentence) != 19:
            v_sentence = v_sentence[:-1]
        v_sentence.append(1)
        
    return v_sentence

def grab_features(story_data, story_keys):
  
    cd = os.getcwd() # get the directory of the pickle files

    features = []
    img_names = []
    all_sentences = []

    for key in story_keys: # grab the story_ids
        for i in range(5):
            image = story_data[key]['images'][i]

            sentence = story_data[key]['sentences'][i]
        
            if image + '.pkl' in os.listdir(cd): # check if in pickle_dir
                
                pkl_file = open(image + '.pkl', 'rb') # open pickle file
                one_feature = pkl.load(pkl_file) # grab feature
                
                features.append(one_feature) # store features
                img_names.append(int(image)) # stores the id of the image
                all_sentences.append(sentence)

                # if len(all_sentences)%100 == 0:
                #     print(len(all_sentences))
                if len(all_sentences) == 7168: # 7168
                    break
            if len(all_sentences) == 7168:
                    break
        if len(all_sentences) == 7168:
                    break
            
        # if len(all_sentences) == 512: #48768
        #     break

    print(f'Finished! Length of features: {len(features)}')

    return features, img_names, all_sentences

def vect_sentences(sentences, vocab):

    vector_sentences = []

    for sentence in sentences: # grab each sentence

        res = re.findall(r'\w+', sentence) # grabs only the words of the sentence

        v_sentence = [] # vectorize the sentence
        for word in res:
            word = word.lower()
            v_word = vocab[word]
            v_sentence.append(v_word)

            # add the padding
        v_sentence = padding(v_sentence)

        vector_sentences.append(v_sentence) # store the set of 5 sentences
           
    print(f'Finished! Length of sentences: {len(vector_sentences)}') 

    return vector_sentences