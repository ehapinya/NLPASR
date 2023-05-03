import pandas as pd

data = [['000'+str(i), 'en', 'en/1.wav',16000] for i in range(1,31)]
cols = ['id', 'lang', 'path', 'sr']
df = pd.DataFrame(data, columns=cols)
df["text"] = [  "The cat sat on the mat.",    \
                "I am running late for my appointment.",    \
                "She is studying hard for her final exams.",    \
                "They have been traveling around Europe for a month.",    \
                "He gave the book to her as a gift.",    \
                "We went to the store and bought some groceries.",    \
                "The sun was shining brightly in the sky.",    \
                "She danced gracefully across the stage.",    \
                "They drove to the beach and spent the day there.",    \
                "He wrote a letter to his friend to apologize.",    \
                "I have never been to Australia before.",    \
                "She sings beautifully and has a great voice.",    \
                "They decided to go out for dinner instead of cooking.",    \
                "He asked her if she wanted to go for a walk.",    \
                "We are going to the concert tonight.",    \
                "The teacher gave the students a difficult assignment.",    \
                "She is always helping others and volunteering her time.",    \
                "They are planning a surprise party for their friend's birthday.",    \
                "He enjoys playing soccer in his free time.",    \
                "I can't believe how quickly the time is passing.",    \
                "She was reading a book when I entered the room.",    \
                "They will be arriving at the airport in a few hours.",    \
                "He was walking his dog when he saw his neighbor.",    \
                "We should go to bed early so we can wake up refreshed.",    \
                "The cat, which was black and white, was chasing a mouse.",   \
                "She drove to work even though it was raining heavily.",    \
                "They are trying to save money for their vacation.",    \
                "He listened carefully to the instructions before beginning.",    \
                "We need to finish this project before the deadline.",    \
                "I am a computer engineeing student."  ]
df["text"] = df["text"].apply(lambda x: x[:-1].upper())
df.to_csv("ref_hyp.csv")
