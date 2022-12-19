import Foldername
import pickle, os

model_folder_name = Foldername.MODEL_FOLDER_NAME


def get_charges(Avg_Session_Length, Time_on_App, Length_of_Membership):
    print("Charges API Testing")

    linear_model = pickle.load(open(f"{model_folder_name}/pricepickle.pkl", 'rb'))

    pred = linear_model.predict([[Avg_Session_Length, Time_on_App, Length_of_Membership]])

    return pred[0] 