states = ['[START]', 'noun', 'verb', '[END]']

# transition probabilities
trans_probs = {('[START]', 'verb'): 0.2,
               ('[START]', 'noun'): 0.8,
               ('noun', 'verb'): 0.8,
               ('noun', '[END]'): 0.1,
               ('noun', 'noun'): 0.1,
               ('verb', 'noun'): 0.2,
               ('verb', 'verb'): 0.1,
               ('verb', '[END]'): 0.7
               }

# emission probabilities
emis_probs = {('noun', 'fish'): 0.8,
              ('noun', 'sleep'): 0.2,
              ('verb', 'fish'): 0.5,
              ('verb', 'sleep'): 0.5
              }

s = 'fish sleep'



def forward(text, states, trans, emis):
    text = ['[START]'] + text.split() + ['[END]']
    length = len(text)
    height = len(states)
    probs = []
    for i in range(height):
        probs.append([])
        for j in range(length):
            probs[i].append(0)
    print(probs)
    backpoint = probs[:]
    probs[0][0] = 1
    probs[1][1] = emis[(states[1], text[1])] * trans[(states[0], states[1])]
    probs[2][2] = emis[(states[2], text[2])] * trans[(states[1], states[2])]
    probs[3][3] = 1
    print(probs)
    # print(probs)
    # for i in range(length):
    #     prev_prob = max(probs[a][i-1] for a in range(height))
    #     print(prev_prob)
        # prev_state
        # for j in range(height):
        #     states[j] text[i]


print(forward(s, states, trans_probs, emis_probs))
