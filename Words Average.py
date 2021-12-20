
# coding: utf-8

# In[50]:


def average_word(word1, word2):
    word1_length = len(word1)
    word2_length = len(word2)

    words_length_average = (word1_length + word2_length)//2
    half_of_average = words_length_average//2
    first_letters = word1[0:half_of_average]
    last_letters = word2[-half_of_average:]
    
    new_word = first_letters + last_letters
    return new_word


# In[76]:


def average_letters(word1, word2):
    word1_length = len(word1)
    word2_length = len(word2)

    words_length_average = (word1_length + word2_length)//2
    half_of_average = words_length_average//2
    first_letters = word1[0:half_of_average]
    last_letters = word2[-half_of_average:]
    
    first_letters_list = []
    last_letters_list = []
    averaged_letters_list = []
    new_word = []
    
    for letter in first_letters:
        first_letters_list.append(ord(letter.lower()))
    for letter in last_letters:
        last_letters_list.append(ord(letter.lower()))
        
    for first_letter in first_letters_list:
        for last_letter in last_letters_list:
            averaged_letters_list.append((first_letter + last_letter)//2)
            
    for number in averaged_letters_list:
        new_word.append(chr(number))
        
    readable_new_word = "".join(new_word)
    
    return readable_new_word
    


# In[122]:


average_word("dark", "souls")


# In[123]:


average_letters("dark", "souls")

