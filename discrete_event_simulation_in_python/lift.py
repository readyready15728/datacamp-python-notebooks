import numpy as np
import pandas as pd
import plotly.express as px


def lift_discrete_event_model(sim_time, number_hotel_floors, lift_people_capacity, travel_time_between_floors, stop_time_open_doors):
    NTS = sim_time
    NF = number_hotel_floors
    LC = lift_people_capacity
    TTpF = travel_time_between_floors
    ST = stop_time_open_doors
    
    LP, PinL = 0, 0

    WTpF, PWpF, cNam = np.zeros(NF + 1), np.zeros(NF + 1), ["Time [min]", "Hotel Floor", "Waiting Time [m]",
                                                            "# People Waiting"]
    df = pd.DataFrame({cNam[0]: [0], cNam[1]: [0], cNam[2]: [0], cNam[3]: [0]})  # Initiating the Dataframe
	
    t, nts_i = 0, 0
    
    while nts_i < NTS:  # Time loop (discrete-event simulation model)
      
       	t += 1
        nts_i = t * TTpF
        
        """
		
        FR = [rd.randint(1, NF), max(math.ceil(rd.gauss(0, 2)), 1)]  # Step_1
        PWpF[FR[0]], WTpF[FR[0]] = PWpF[FR[0]] + FR[1], WTpF[FR[0]] + TTpF  # Step_2
        WTpF = np.array([x + TTpF if x > 0 else x for x in WTpF])  # Step_3
        TF = WTpF.argmax() if PinL < LC else 0  # Step_4
        PEL, WTpF[LP] = min(PWpF[LP], LC - PinL) if TF == LP else 0, 0 if TF == LP else WTpF[LP]  # Step_5
        PinL, PWpF[LP] = PinL + PEL if TF == LP else PinL, PWpF[LP] - PEL if TF == LP else PWpF[LP]  # Step_6
        LP, PinL = LP + 1 if TF > LP else LP - 1 if TF < LP else LP, 0 if LP == 0 else PinL  # Step_7
        df = pd.concat([df, pd.DataFrame({cNam[0]: [t * TTpF], cNam[1]: [LP], cNam[2]: [PinL], cNam[3]: [PinL]})])  # Step_8
        df = pd.concat([df, pd.DataFrame([{cNam[0]: t * TTpF, cNam[1]: nf, cNam[2]: WTpF[nf], cNam[3]: PWpF[nf]}
                                          for nf in range(NF + 1)])])  # Step_9
                                          
    	"""
    
    df = pd.read_csv("lift_df.csv")

    fig = px.scatter(df, x=cNam[0], y=cNam[1], color=cNam[2], size=cNam[3], size_max=max(df[cNam[3]]), animation_frame=cNam[0],
               range_color=(min(df[cNam[2]]), max(df[cNam[2]])), range_x=(0, t * TTpF),
               range_y=(0, NF + 1), text = cNam[3])  # Step_10
    
    fig.update_yaxes(range = [0, 7.5])
    
    fig.update_traces(textposition='middle right', textfont=dict(
        family="sans serif",
        size=10,
        color="black"))
    
    fig.add_annotation(text="> Color of circles: waiting time in each floor",
                  xref="paper", yref="paper",
                  x=0, y=1, showarrow=False)
    
    fig.add_annotation(text="> Size and text in circles: number of people waiting in each floor",
                  xref="paper", yref="paper",
                  x=0, y=0.92, showarrow=False)
    
    fig.add_annotation(text="> Moving circle: Lift",
                  xref="paper", yref="paper",
                  x=0, y=0.84, showarrow=False)
    
    fig.show()
    
    df_results = df
    
    return df


# Floor and lift parameters
number_hotel_floors = 5
lift_people_capacity = 15
travel_time_between_floors = 3/60
stop_time_open_doors = 6/60
sim_time = 5

# Run the model
df_results = lift_discrete_event_model(sim_time, number_hotel_floors, lift_people_capacity, travel_time_between_floors, stop_time_open_doors)
