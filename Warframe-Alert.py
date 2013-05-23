import urllib.request
import xml.etree.ElementTree as ET
import datetime
req = urllib.request.Request('http://content.playwarframe.com/alerts.xml')

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


r = urllib.request.urlopen(req)
sitestring=r.read()
sitestring=sitestring.replace(b'wf:', b'')
root=ET.fromstring(sitestring)
items=root.find('channel').findall('item')
for alert in items:
  alertText=alert.find('title').text
  alertArray=alertText.split(' - ')
  timeEnd = datetime.datetime.strptime(alert.find('expiry').text, "%a, %d %b %Y %H:%M:%S %z")
  timeNow = datetime.datetime.now(datetime.timezone.utc)
  timeLeft = timeEnd - timeNow
  isActive = timeEnd > timeNow
  if (isActive):
    print(alertText, "-", timeLeft)
    if (minimumCredits < int(alertArray[2][:-2]) or (len(alertArray)==4 and alertArray[3] not in rewardsToIgnore)):
      print("EPIC")
