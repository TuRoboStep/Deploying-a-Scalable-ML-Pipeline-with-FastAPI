# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

Model type: Random Forest by scykitlearn
Model date: 03.01.2024
Model version: scikit-learn==1.5.1

A random forest is a meta estimator that fits a number of decision tree
classifiers on various sub-samples of the dataset and uses averaging to
improve the predictive accuracy and control over-fitting.

Number of trees used: 100

The model is used "off the shelf" from the scykitlearn library.
Further details can be found in the [scykitlearn documentation](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

## Intended Use

Primary intended uses:
- classification of salaries to <= 50k and >50k from the census data

primary intended users:
- Developers and ML enthusiasts that want to classify the data and try out this classifier

Out of scope use cases:
- Since this is just an example implementation, everything beyond the census dataset is out of scope for now

## Training Data

The traning data is the census.csv in the projects `data` folder. The training cata is a 80% split from all the data. It contains categorical and numerical
features. The project only uses: workclass, education, marital-status, occupation, relationship, race, sex, native-country.
The intend is to build a classifier for binary salary classification.

## Evaluation Data

The remaining 20% split from the census data on the `data` folder. I contains the same features and the same intend ans the trainin data.

## Metrics

### Metrics Summary

Precision: 0.7321 
Recall: 0.6431 
F1: 0.6848

Precision: The precision varies across different categories, with the highest being 1.0000 and the lowest around 0.5000.
Recall: Recall also varies significantly, with some categories having a recall of 1.0000 and others much lower.
F1 Score: The F1 score ranges from perfect 1.0000 to lower scores where precision and recall are not balanced.

### Example details
#### Workclass:
Federal-gov:
Precision: 0.9385, Recall: 0.9616, F1: 0.9499
The high recall indicates that the model correctly identifies most instances for this class.

Without-pay:
Precision: 1.0000, Recall: 1.0000, F1: 1.0000
Perfect scores, likely due to the very low count (1 instance).

Private:
Precision: 0.9515, Recall: 0.9212, F1: 0.9361
Large sample size (4,452), the model generalizes well.

#### Education:
1st-4th:
Precision: 1.0000, Recall: 0.6667, F1: 0.8000
High precision but lower recall indicates many false negatives.

Doctorate:
Precision: 0.9512, Recall: 0.9750, F1: 0.9630
High metrics, indicating good performance on this relatively small group (72 instances).

Preschool:
Precision: 1.0000, Recall: 1.0000, F1: 1.0000
Perfect scores, similar to the workclass: Without-pay, due to very low count (9 instances).

### Conclusion
The results show that the model's performance varies across different categories within each feature. While the model performs well for most categories with high precision and recall, there are specific categories where the performance is notably lower, such as native-country: Columbia and education: 1st-4th.

The model demonstrates strong performance for large groups like workclass: Private and native-country: United-States, indicating good generalizability. However, categories with very small sample sizes tend to have perfect scores, which might be misleading due to the lack of sufficient data.

Overall, the model shows a balanced performance with some areas needing improvement for specific underrepresented groups.

## Ethical Considerations

The "race" in the data in long tail distributed, which means that most of the people were captured to one category (white >>50%) and the other categories are underrepresented. The model learned this distribution and is therefore biased towards it. This can result in wrong categorization in the less dominant categories as well as wrong interpretations of the results for such examples. As we have seen in the Metrics section, it's possible for the model to simply learn the prediction by heart for rare exmaples leading to good predictions in this specific case but not generalizing well. It's also possible that the model will perform worse on rare categories because it has hearned that getting them right is not reducing the loss very much.

## Caveats and Recommendations

The model used here is rather simple, one can use a more sophisticated model (deep learning) or a larges set of trees here. Also XGBoost usually creates good performance on this kind of data. Therefore this model-selection has not been optimized to the best performance. Also the data contains a large imbalance in some categories like "race" as mentioned above. For better performance, it would be great to capture more data in the less represented categories, to account for the imbalance, or use proper loss weighting techniques to make the model more general.