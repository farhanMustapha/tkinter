import tkinter as tk
import mysql.connector

class Mission:
    def __init__(self, date, activite, lieu, chauffeur, km):
        self.date = date
        self.activite = activite
        self.lieu = lieu
        self.chauffeur = chauffeur
        self.km = km

    def save_to_db(self):
        # Connect to the database
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="voiture"
        )

        cursor = con.cursor()

        # Insert the data into the table
        sql = "INSERT INTO missions (date, activite, lieu, chauffeur, km) VALUES (%s, %s, %s, %s, %s)"
        values = (self.date, self.activite, self.lieu, self.chauffeur, self.km)
        cursor.execute(sql, values)

        con.commit()

        # Close the connection
        con.close()

class MissionApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # UI elements and layout
    
        # Date Label
        self.date_label = tk.Label(self, text="Date:")
        self.date_label.grid(row=0,column=0)

        # Date Entry
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=0,column=1)

        # Activite Label
        self.activite_label = tk.Label(self, text="Activite:")
        self.activite_label.grid(row=1,column=0)

        # Activite Entry
        self.activite_entry = tk.Entry(self)
        self.activite_entry.grid(row=1,column=1)

        # Lieu Label
        self.lieu_label = tk.Label(self, text="Lieu:")
        self.lieu_label.grid(row=2,column=0)

        # Lieu Entry
        self.lieu_entry = tk.Entry(self)
        self.lieu_entry.grid(row=2,column=1)

        # Chauffeur Label
        self.chauffeur_label = tk.Label(self, text="Chauffeur:")
        self.chauffeur_label.grid(row=3,column=0)

        # Chauffeur Entry
        self.chauffeur_entry = tk.Entry(self)
        self.chauffeur_entry.grid(row=3,column=1)
        
        # km Label
        self.km_label = tk.Label(self, text="KM:")
        self.km_label.grid(row=4,column=0)

        # km Entry
        self.km_entry = tk.Entry(self)
        self.km_entry.grid(row=4,column=1)

        # Create Button
        self.create_button = tk.Button(self, text="Create", command=self.create_mission)
        self.create_button.grid(row=6,column=1)

    def create_mission(self):
        date = self.date_entry.get()
        activite = self.activite_entry.get()
        lieu = self.lieu_entry.get()
        chauffeur = self.chauffeur_entry.get()
        km = self.km_entry.get()
        new_mission = Mission(date, activite, lieu, chauffeur, km)
        print(new_mission.__dict__)

    def create_mission(self):
        date = self.date_entry.get()
        activite = self.activite_entry.get()
        lieu = self.lieu_entry.get()
        chauffeur = self.chauffeur_entry.get()
        km = self.km_entry.get()
        new_mission = Mission(date, activite, lieu, chauffeur, km)
        new_mission.save_to_db()

app = MissionApp()
app.mainloop()
