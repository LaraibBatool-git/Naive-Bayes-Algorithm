# Naive Bayes Classifier from Scratch (Play Cricket)

A simple Python implementation of the **Naive Bayes algorithm** using the classic "play cricket" weather dataset. It calculates every probability step by step with pandas so the algorithm is easy to follow, and then predicts whether cricket will be played on a new day.

## What the program does

1. Loads the dataset from `Data.csv`.
2. Calculates the **prior probabilities**: P(Yes) and P(No).
3. Calculates the **likelihoods** for each feature given each class, for example P(Sunny | Yes) and P(Strong | No).
4. Applies the **Naive Bayes formula** to a new day's conditions and predicts Yes or No.

## How Naive Bayes works

For a new day with features Outlook, Temperature, Humidity and Wind:

```
Score(Yes) = P(Yes) x P(Outlook|Yes) x P(Temperature|Yes) x P(Humidity|Yes) x P(Wind|Yes)
Score(No)  = P(No)  x P(Outlook|No)  x P(Temperature|No)  x P(Humidity|No)  x P(Wind|No)
```

The class with the higher score is the prediction. The two scores can also be normalized so they add up to 1:

```
P(Yes | conditions) = Score(Yes) / (Score(Yes) + Score(No))
```

It is called "naive" because it assumes the features are independent of each other given the class.

## Dataset

`Data.csv` has 14 rows and 5 columns:

| Column        | Values                      |
|---------------|-----------------------------|
| Outlook       | Sunny, Overcast, Rainy      |
| Temperature   | Hot, Mild, Cool             |
| Humidity      | High, Normal                |
| Wind          | Weak, Strong                |
| PlayCricket   | Yes, No (the target column) |

The dataset has 9 "Yes" rows and 5 "No" rows.

> The column names in the CSV header must match the names used in the code exactly (for example `Temperature`, not `Temp`).

## Requirements

- Python 3.8 or newer
- pandas

Install pandas with:

```
python -m pip install pandas
```

## How to run

1. Put `Data.csv` in the same folder as the Python file (or change the path in `pd.read_csv`).
2. Run the program:

```
python NB.py
```

## Example

For a new day with **Sunny, Cool, High, Strong**:

| Quantity        | Value |
|-----------------|-------|
| Score(Yes)      | 0.0053 |
| Score(No)       | 0.0206 |
| P(Yes)          | 0.205 |
| P(No)           | 0.795 |
| **Prediction**  | **No** (cricket will not be played) |

To test a different day, change these variables near the end of the script:

```python
outlook = 'Sunny'
temp = 'Cool'
humidity = 'High'
wind = 'Strong'
```

## Limitations

- **Zero probability problem:** if a feature value never appears with a class in the training data, its probability is 0 and the whole product becomes 0. Laplace smoothing (add 1 to each count and the number of unique values to the denominator) fixes this.
- **Independence assumption:** real-world features are rarely fully independent, although Naive Bayes often still works well on small datasets.
- The dataset is very small, so this is for learning, not for real predictions.

## Possible improvements

- Add Laplace smoothing.
- Take the new day's conditions from user input with `input()`.
- Wrap the calculations in functions or a class.
- Compare the result with scikit-learn's `CategoricalNB`.
