from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% Load datasets
def load_datasets():
    world_cup = pd.read_csv('World Cup 2019 Dataset.csv')
    results = pd.read_csv('results.csv')
    return world_cup, results

# %% Filter results for a specific team
def filter_team_results(results, team):
    return results[(results["Team_1"] == team) | (results["Team_2"] == team)]

# %% Create a column for matches played in or after 2010
def filter_matches_after_2010(df):
    df['matchyear'] = df['date'].apply(lambda x: int(x.split('/')[-1]))
    return df[df['matchyear'] >= 10]

# %% Filter results for World Cup teams
def filter_worldcup_teams(results, worldcup_teams):
    df_team_1 = results[results["Team_1"].isin(worldcup_teams)]
    df_team_2 = results[results["Team_2"].isin(worldcup_teams)]
    df_teams = pd.concat([df_team_1, df_team_2]).drop_duplicates()
    return df_teams

# %% Drop irrelevant columns
def drop_irrelevant_columns(df, columns_to_drop):
    return df.drop(columns=columns_to_drop, axis=1)

# %% Prepare dataset for modeling
def prepare_modeling_data(df):
    df = df.reset_index(drop=True)
    df['winning_team'] = np.where(df['Winner'] == df['Team_1'], 1, 2)
    df = df.drop(['winning_team'], axis=1)
    return df

# %% One-hot encode categorical variables
def one_hot_encode(df, columns):
    return pd.get_dummies(df, prefix=columns, columns=columns)

# %% Train logistic regression model
def train_model(X_train, y_train):
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)
    return logreg

# %% Add ICC rankings to fixtures
def add_icc_rankings(fixtures, ranking):
    fixtures = fixtures.copy()
    fixtures['first_position'] = fixtures['Team_1'].map(ranking.set_index('Team')['Position'])
    fixtures['second_position'] = fixtures['Team_2'].map(ranking.set_index('Team')['Position'])
    return fixtures

# %% Create prediction dataset based on ICC rankings
def create_prediction_set(fixtures):
    pred_set = []
    for _, row in fixtures.iterrows():
        if row['first_position'] < row['second_position']:
            pred_set.append({'Team_1': row['Team_1'], 'Team_2': row['Team_2'], 'winning_team': None})
        else:
            pred_set.append({'Team_1': row['Team_2'], 'Team_2': row['Team_1'], 'winning_team': None})
    return pd.DataFrame(pred_set)

# %% Predict match outcomes
def predict_outcomes(pred_set, final_columns, logreg, backup_pred_set):
    pred_set = one_hot_encode(pred_set, ['Team_1', 'Team_2'])
    for c in set(final_columns) - set(pred_set.columns):
        pred_set[c] = 0
    pred_set = pred_set[final_columns].drop(['Winner'], axis=1)
    predictions = logreg.predict(pred_set)
    for i, row in backup_pred_set.iterrows():
        print(f"{row['Team_1']} and {row['Team_2']}")
        if predictions[i] == 1:
            print(f"Winner: {row['Team_1']}")
        else:
            print(f"Winner: {row['Team_2']}")
        print("")

# %% Prediction function for specific matches
def predict(matches, ranking, final, logreg):
    positions = [(ranking.loc[ranking['Team'] == match[0], 'Position'].iloc[0], 
                  ranking.loc[ranking['Team'] == match[1], 'Position'].iloc[0]) for match in matches]
    pred_set = [{'Team_1': match[0] if pos[0] < pos[1] else match[1], 
                 'Team_2': match[1] if pos[0] < pos[1] else match[0]} for match, pos in zip(matches, positions)]
    backup_pred_set = pd.DataFrame(pred_set)
    predict_outcomes(pd.DataFrame(pred_set), final.columns, logreg, backup_pred_set)

# %% Main execution
def main():
    # Load datasets
    world_cup, results = load_datasets()

    # Filter results for Pakistan
    pak = filter_team_results(results, "Pakistan")
    pak_2010 = filter_matches_after_2010(pak)

    # World Cup teams
    worldcup_teams = ['England', 'South Africa', 'West Indies', 'Pakistan', 'New Zealand', 
                      'Sri Lanka', 'Afghanistan', 'Australia', 'Bangladesh', 'India']

    # Filter results for World Cup teams
    df_teams = filter_worldcup_teams(results, worldcup_teams)
    df_teams = drop_irrelevant_columns(df_teams, ["date", "Margin", "Ground"])

    # Prepare dataset for modeling
    df_teams = prepare_modeling_data(df_teams)

    # One-hot encode and split data
    final = one_hot_encode(df_teams, ['Team_1', 'Team_2'])
    X = final.drop(['Winner'], axis=1)
    y = final['Winner']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    # Train logistic regression model
    logreg = train_model(X_train, y_train)
    print(f"Training set accuracy: {logreg.score(X_train, y_train):.3f}")
    print(f"Test set accuracy: {logreg.score(X_test, y_test):.3f}")

    # Load new datasets for rankings and fixtures
    ranking = pd.read_csv('icc_rankings.csv')
    fixtures = pd.read_csv('fixtures.csv')

    # Add ICC rankings to fixtures
    fixtures = add_icc_rankings(fixtures, ranking)
    fixtures = fixtures.iloc[:45, :]

    # Create prediction set and backup
    pred_set = create_prediction_set(fixtures)
    backup_pred_set = pred_set.copy()

    # Predict outcomes for group matches
    print("Group Matches Predictions:")
    predict_outcomes(pred_set, final.columns, logreg, backup_pred_set)

    # Semi-finals and Finals predictions
    semi_finals = [('New Zealand', 'India'), ('England', 'Australia')]
    print("-------SEMI FINALS----- ")
    predict(semi_finals, ranking, final, logreg)

    finals = [('India', 'England')]
    print("WINNER OF ICC CWC 2019")
    predict(finals, ranking, final, logreg)

if __name__ == "__main__":
    main()
