import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Use os.path.join if needed
test_data_dir = os.getenv("test_data_dir")
validation_data_dir = os.getenv("validation_data_dir")
train_data_dir = os.getenv("train_data_dir")

print("Test dir:", test_data_dir)
print("Validation dir:", validation_data_dir)
print("Train dir:", train_data_dir)

# Optional: verify existence
for path in [test_data_dir, validation_data_dir, train_data_dir]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing directory: {path}")

print("✅ All dataset directories verified.")

# ✅ Check if required files exist
required_test_files = [
    "dialogues_test.txt",
    "dialogues_act_test.txt",
    "dialogues_emotion_test.txt"
]

for file in required_test_files:
    path = os.path.join(test_data_dir, file)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing file: {path}")

# ✅ Load dialogues
dialogues = []
with open(os.path.join(test_data_dir, "dialogues_test.txt"), "r", encoding="utf-8") as f:
    for line in f:
        dialogues.append(line.strip().split("\t"))

# ✅ Load act labels
acts = []
with open(os.path.join(test_data_dir, "dialogues_act_test.txt"), "r", encoding="utf-8") as f:
    for line in f:
        acts.append([int(x) for x in line.strip().split()])

# ✅ Load emotion labels
emotions = []
with open(os.path.join(test_data_dir, "dialogues_emotion_test.txt"), "r", encoding="utf-8") as f:
    for line in f:
        emotions.append([int(x) for x in line.strip().split()])

# ✅ Flatten all utterances, emotions, and acts
utterances_all = []
emotions_all = []
acts_all = []

for dlg, emos, whys in zip(dialogues, emotions, acts):
    splits = dlg[0].split('__eou__')
    splits = [utt.strip() for utt in splits if utt.strip()]

    # append emotion-utterance pairs
    for utt, emo in zip(splits, emos):
        utterances_all.append(utt)
        emotions_all.append(emo)

    # append act labels
    for why in whys:
        acts_all.append(why)

# ✅ Mapping dictionaries
emotion_map = {
    0: "other",
    1: "anger",
    2: "disgust",
    3: "fear",
    4: "happiness",
    5: "sadness",
    6: "surprise",
}

act_map = {
    1: "inform",
    2: "question",
    3: "directive",
    4: "commissive"
}

# ✅ Create DataFrame
df_full = pd.DataFrame({
    "utterance": utterances_all,
    "emotion_id": emotions_all,
    "acts_id": acts_all
})

df_full["emotion"] = df_full["emotion_id"].map(emotion_map)
df_full["acts"] = df_full["acts_id"].map(act_map)

# ✅ Print distribution of emotion labels
print("\nEmotion label distribution:")
print(df_full["emotion"].value_counts())

# ✅ Save to CSV
output_path = os.path.join(os.getcwd(), "testdata.csv")
df_full.to_csv(output_path, index=False)
print(f"\nData saved successfully to {output_path}")


#--------------------------------------------------------------------------------------------------
# ✅ Use raw string to avoid invalid escape sequences

# ✅ Check if required files exist
required_validation_files = [
    "dialogues_validation.txt",
    "dialogues_act_validation.txt",
    "dialogues_emotion_validation.txt"
]

for file in required_validation_files:
    path = os.path.join(validation_data_dir, file)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing file: {path}")

# ✅ Load dialogues
dialogues = []
with open(os.path.join(validation_data_dir, "dialogues_validation.txt"), "r", encoding="utf-8") as f:
    for line in f:
        dialogues.append(line.strip().split("\t"))

# ✅ Load act labels
acts = []
with open(os.path.join(validation_data_dir, "dialogues_act_validation.txt"), "r", encoding="utf-8") as f:
    for line in f:
        acts.append([int(x) for x in line.strip().split()])

# ✅ Load emotion labels
emotions = []
with open(os.path.join(validation_data_dir, "dialogues_emotion_validation.txt"), "r", encoding="utf-8") as f:
    for line in f:
        emotions.append([int(x) for x in line.strip().split()])

# ✅ Flatten all utterances, emotions, and acts
utterances_all = []
emotions_all = []
acts_all = []

for dlg, emos, whys in zip(dialogues, emotions, acts):
    splits = dlg[0].split('__eou__')
    splits = [utt.strip() for utt in splits if utt.strip()]

    # append emotion-utterance pairs
    for utt, emo in zip(splits, emos):
        utterances_all.append(utt)
        emotions_all.append(emo)

    # append act labels
    for why in whys:
        acts_all.append(why)

# ✅ Mapping dictionaries
emotion_map = {
    0: "other",
    1: "anger",
    2: "disgust",
    3: "fear",
    4: "happiness",
    5: "sadness",
    6: "surprise",
}

act_map = {
    1: "inform",
    2: "question",
    3: "directive",
    4: "commissive"
}

# ✅ Create DataFrame
df_full = pd.DataFrame({
    "utterance": utterances_all,
    "emotion_id": emotions_all,
    "acts_id": acts_all
})

df_full["emotion"] = df_full["emotion_id"].map(emotion_map)
df_full["acts"] = df_full["acts_id"].map(act_map)

# ✅ Print distribution of emotion labels
print("\nEmotion label distribution:")
print(df_full["emotion"].value_counts())

# ✅ Save to CSV
output_path = os.path.join(os.getcwd(), "validationdata.csv")
df_full.to_csv(output_path, index=False)
print(f"\nData saved successfully to {output_path}")

#--------------------------------------------------------------------------------------------------


# ✅ Use raw string to avoid invalid escape sequences

# ✅ Check if required files exist
required_train_files = [
    "dialogues_train.txt",
    "dialogues_act_train.txt",
    "dialogues_emotion_train.txt"
]

for file in required_train_files:
    path = os.path.join(train_data_dir, file)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing file: {path}")

# ✅ Load dialogues
dialogues = []
with open(os.path.join(train_data_dir, "dialogues_train.txt"), "r", encoding="utf-8") as f:
    for line in f:
        dialogues.append(line.strip().split("\t"))

# ✅ Load act labels
acts = []
with open(os.path.join(train_data_dir, "dialogues_act_train.txt"), "r", encoding="utf-8") as f:
    for line in f:
        acts.append([int(x) for x in line.strip().split()])

# ✅ Load emotion labels
emotions = []
with open(os.path.join(train_data_dir, "dialogues_emotion_train.txt"), "r", encoding="utf-8") as f:
    for line in f:
        emotions.append([int(x) for x in line.strip().split()])

# ✅ Flatten all utterances, emotions, and acts
utterances_all = []
emotions_all = []
acts_all = []

for dlg, emos, whys in zip(dialogues, emotions, acts):
    splits = dlg[0].split('__eou__')
    splits = [utt.strip() for utt in splits if utt.strip()]

    # append emotion-utterance pairs
    for utt, emo in zip(splits, emos):
        utterances_all.append(utt)
        emotions_all.append(emo)

    # append act labels
    for why in whys:
        acts_all.append(why)

# ✅ Mapping dictionaries
emotion_map = {
    0: "other",
    1: "anger",
    2: "disgust",
    3: "fear",
    4: "happiness",
    5: "sadness",
    6: "surprise",
}

act_map = {
    1: "inform",
    2: "question",
    3: "directive",
    4: "commissive"
}

# ✅ Create DataFrame
df_full = pd.DataFrame({
    "utterance": utterances_all,
    "emotion_id": emotions_all,
    "acts_id": acts_all
})

df_full["emotion"] = df_full["emotion_id"].map(emotion_map)
df_full["acts"] = df_full["acts_id"].map(act_map)

# ✅ Print distribution of emotion labels
print("\nEmotion label distribution:")
print(df_full["emotion"].value_counts())

# ✅ Save to CSV
output_path = os.path.join(os.getcwd(), "traindata.csv")
df_full.to_csv(output_path, index=False)
print(f"\nData saved successfully to {output_path}")