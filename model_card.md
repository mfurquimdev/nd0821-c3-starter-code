# Model Card

Predict whether income exceeds $50K/yr based on census data. Also known as "Adult" dataset.
This data set was donated by Ronny Kohavi <ronnyk@sgi.com> and Barry Becker.
Extraction was done by Barry Becker from the 1994 Census database.

Source of data
https://archive.ics.uci.edu/ml/datasets/census+income

## Model Details

The model type is a `RandomForestClassifier` with `max_depth=25`, `n_estimators=30`, and `max_features=14`.
These hyperparameters were chosen arbitrary after a few trial and error.

## Intended Use

This model is to be used for inferring whether a person's annual earnings are greater than $50,000.00.

## Data

The `census.csv` had extra spaces which was removed using a sed script:

```bash
sed -i -e "s, ,,g" census.csv
```

The data was then loaded into a pandas DataFrame
and split into training set and test set using `train_test_split` with `test_size=0.20`.
In both data set the categorical features were separated and used `OneHotEncoder` to encode
and the label was transformed using a `LabelBinarizer`.

## Bias

After running the `pandas_profiling` in the data, the following imbalances were found:

- The `capital-gain` and `capital-loss` have over 90% of zero values.
- Almost 70% of `workclass` category values are `Private`.
- Approximately 85% of `race` category values are `White`.
- There is an imbalance on `sex` category, which ~67% is `Male` and ~33% is `Female`.
- Almost 90% of `native-country` is `United-States`.
- At last, there is also an imbalance on `salary` category, which ~76% is `<=50K` and ~24% is `>50K`.

## Metrics

After training the model, the test set was used to calculate precision, recall and fbeta metrics.
The precision is 0.751. The recall is 0.615. And the fbeta is 0.676.

There's more metrics for each data slice on [slice_output.txt](slice_output.txt).

## Caveats and Recommendations

There is a huge imbalance on the `native-country` category.
It would probably help if there were more data with values other than `United-States`.

## Attribute Information

Listing of attributes and its values

### Label

#### salary
- <=50K
- \>50K

### Continuous

- age
- capital-gain
- capital-loss
- education-num
- fnlwgt
- hours-per-week


### Categorical

#### workclass
- Federal-gov
- Local-gov
- Never-worked
- Private
- Self-emp-inc
- Self-emp-not-inc
- State-gov
- Without-pay

#### education
- 10th
- 11th
- 12th
- 1st-4th
- 5th-6th
- 7th-8th
- 9th
- Assoc-acdm
- Assoc-voc
- Bachelors
- Doctorate
- HS-grad
- Masters
- Preschool
- Prof-school
- Some-college

#### marital-status
- Divorced
- Married-AF-spouse
- Married-civ-spouse
- Married-spouse-absent
- Never-married
- Separated
- Widowed

#### occupation
- Adm-clerical
- Armed-Forces
- Craft-repair
- Exec-managerial
- Farming-fishing
- Handlers-cleaners
- Machine-op-inspct
- Other-service
- Priv-house-serv
- Prof-specialty
- Protective-serv
- Sales
- Tech-support
- Transport-moving

#### relationship
- Husband
- Not-in-family
- Other-relative
- Own-child
- Unmarried
- Wife

#### race
- Amer-Indian-Eskimo
- Asian-Pac-Islander
- Black
- Other
- White

#### sex
- Female
- Male

#### native-country
- Cambodia
- Canada
- China
- Columbia
- Cuba
- Dominican-Republic
- Ecuador
- El-Salvador
- England
- France
- Germany
- Greece
- Guatemala
- Haiti
- Holand-Netherlands
- Honduras
- Hong
- Hungary
- India
- Iran
- Ireland
- Italy
- Jamaica
- Japan
- Laos
- Mexico
- Nicaragua
- Outlying-US(Guam-USVI-etc)
- Peru
- Philippines
- Poland
- Portugal
- Puerto-Rico
- Scotland
- South
- Taiwan
- Thailand
- Trinadad&Tobago
- United-States
- Vietnam
- Yugoslavia
