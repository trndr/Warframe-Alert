import urllib.request
import xml.etree.ElementTree as ET
import datetime
import tkinter
import time


minimumCredits=6000
rewards=[
'Orokin Reactor',
'Orokin Catalyst',
'Ash Helmet (Blueprint)',
'Banshee Helmet (Blueprint)',
'Brook Hammer (Blueprint)',
'Ceramic Dagger (Blueprint)',
'Dagger Axe (Blueprint)',
'Dark Dagger (Blueprint)',
'Dark Sword (Blueprint)',
'Dual Dagger (Blueprint)',
'Ember Helmet (Blueprint)',
'Excalibur Helmet (Blueprint)',
'Frost Helmet (Blueprint)',
'Glaive (Blueprint)',
'Heat Dagger (Blueprint)',
'Heat Sword (Blueprint)',
'Jaw Sword (Blueprint)',
'Loki Helmet (Blueprint)',
'Mag Helmet (Blueprint)',
'Nyx Helmet (Blueprint)',
'Pangolin Sword (Blueprint)',
'Plasma Sword (Blueprint)',
'Rhino Helmet (Blueprint)',
'Saryn Helmet (Blueprint)',
'Vauban Helmet (Blueprint)',
'Vauban Chassis (Blueprint)',
'Vauban Systems (Blueprint)',
'Enemy Radar (Artifact)',
'Energy Siphon (Artifact)',
'Physique (Artifact)',
'Rejuvenation (Artifact)'
'Pistol Scavenger (Artifact)',
'Rifle Scavenger (Artifact)',
'Sniper Scavenger (Artifact)',
'Shotgun Scavenger (Artifact)',
'Rifle Amp (Artifact)',
'Steel Charge (Artifact)'
]
rewardsToIgnore = [
'Banshee Helmet (Blueprint)',
'Dagger Axe (Blueprint)',
'Dark Dagger (Blueprint)',
'Dark Sword (Blueprint)',
'Ember Helmet (Blueprint)',
'Excalibur Helmet (Blueprint)',
'Frost Helmet (Blueprint)',
'Jaw Sword (Blueprint)',
'Mag Helmet (Blueprint)',
'Rhino Helmet (Blueprint)',
'Saryn Helmet (Blueprint)',
'Enemy Radar (Artifact)',
'Energy Siphon (Artifact)',
'Physique (Artifact)',
'Pistol Scavenger (Artifact)',
'Rifle Scavenger (Artifact)',
'Sniper Scavenger (Artifact)',
'Shotgun Scavenger (Artifact)',
'Rifle Amp (Artifact)'
]

class GUI:
  def __init__(self):
    self.root = tkinter.Tk()
    self.alertText = tkinter.StringVar()

    frame = tkinter.Frame()
    frame.pack()

    self.button = tkinter.Button(frame, text="QUIT", fg="red", command=frame.quit)
    self.button.pack(side=tkinter.LEFT)

    self.currentAlerts = tkinter.Label(frame, textvariable=self.alertText)
    self.currentAlerts.pack(side=tkinter.LEFT)
    self.hi_there = tkinter.Button(frame, text="Hello", command=self.updateAlerts)
    self.hi_there.pack(side=tkinter.LEFT)
    self.parser = Parser()
    self.fetchAlerts()
    self.updateAlerts()
    self.root.mainloop()
#    self.currentAlerts.set(alertText)
 #   while(True):

  def fetchAlerts(self):
    self.alertRoot = self.parser.fetch()
    self.root.after(120000, self.fetchAlerts)
  def updateAlerts(self):
    self.alertText.set(self.parser.parse(self.alertRoot))
    self.root.after(1000, self.updateAlerts)

class Parser:
  def fetch(self):
    r = urllib.request.urlopen(req)
    sitestring=r.read()
    sitestring=sitestring.replace(b'wf:', b'')
    root=ET.fromstring(sitestring)
    return root
    
  def parse(self, root):
    alertTextCombined = ''
    items=root.find('channel').findall('item')
    for alert in items:
      alertText = alert.find('title').text
      alertArray = alertText.split(' - ')
      timeEnd = datetime.datetime.strptime(alert.find('expiry').text, '%a, %d %b %Y %H:%M:%S %z')
      timeNow = datetime.datetime.now(datetime.timezone.utc)
      timeLeft = timeEnd - timeNow
      isActive = timeEnd > timeNow
      if (isActive):
        alertTextCombined += alertText + ' - ' + str(timeLeft)[2:-7] + '\n'
 #       print(alertText, "-", timeLeft)
        if (minimumCredits < int(alertArray[2][:-2]) or (len(alertArray)==4 and alertArray[3] not in rewardsToIgnore)):
          print("EPIC")
    return alertTextCombined

class Config:
  def __init__(self):
    self.load()
  def load(self):
    xml = ET.parse('config.xml')
    root = xml.getroot()
    global website
    website = root.find("website").text
    rewardArray = []
    rewards = root.find("rewards")
    for rewardType in rewards:
      if (rewardType.tag!="Others"):
        for reward in rewardType:
          rewardArray.append(reward.text +" ("+reward.tag+")")
      else:
        for reward in rewardType:
          rewardArray.append(reward.text)
    print(rewardArray)

    

#website = ''
Config()
req = urllib.request.Request(website)

app = GUI()

#app.mainloop()
