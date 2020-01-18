import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def player_vote(player):
	# Click on vote
	action.move_to_element(player).perform()
	try:
		player.click()
		return True
	except:
		# Not clickable error
		return False

	time.sleep(2)
	
def position_change(xpath):
	addCheck = False
	try:
		position = driver.find_element_by_xpath(xpath)
		action.move_to_element(position).perform()
		position.click()
	except: 
		addCheck = True
	#time.sleep(1)
	return addCheck

def submit():
	submit = driver.find_element_by_xpath('//*[@id="ballot-submit"]')
	action.move_to_element(submit).perform()
	submit.click()

# Control list of lists for infinite iterations
list_of_players = []
qb = []
rb = []
wr = []
fb = []	#No Bears Players
te = []
t = []
g = []
c = []

de = [] #No Bears Players
dt = []
ilb = []
olb = []
cb = []
ss = []
fs = []

k = []
rs = []
p = []
st = []


qb.append('//*[@id="button-QB"]')
qb.append('983040_13_1_29')	#Trubisky
list_of_players.append(qb)

rb.append('//*[@id="button-RB"]')
rb.append('983040_14_1_51')	#Cohen
rb.append('983040_14_1_25')	#Howard
list_of_players.append(rb)

wr.append('//*[@id="button-WR"]')
wr.append('983040_19_1_50') #Miller
wr.append('983040_19_1_56') #Robinson
wr.append('983040_19_1_30') #Gabriel
list_of_players.append(wr)

te.append('//*[@id="button-TE"]')
te.append('983040_18_1_03')
list_of_players.append(te)

t.append('//*[@id="button-T"]')
t.append('983040_17_1_29') #Leno
t.append('983040_17_1_31') #Massie
list_of_players.append(t)

g.append('//*[@id="button-G"]')
g.append('983040_07_1_11') #Daniels
g.append('983040_07_1_61') #Witzman
list_of_players.append(g)

c.append('//*[@id="button-C"]')
c.append('983040_01_1_32') #Whitehair
list_of_players.append(c)

dt.append('//*[@id="button-DT"]')
dt.append('983040_04_1_26') #Hicksy
dt.append('983040_04_1_18') #Goldman
list_of_players.append(dt)

ilb.append('//*[@id="button-ILB"]')
ilb.append('983040_08_1_37') #Roquan
ilb.append('983040_08_1_39') #Trevathan
list_of_players.append(ilb)

olb.append('//*[@id="button-OLB"]')
olb.append('983040_11_1_20') #Floyd
olb.append('983040_11_1_36') #Mack
list_of_players.append(olb)

cb.append('//*[@id="button-CB"]')
cb.append('983040_02_1_03') #Prince
cb.append('983040_02_1_18') #Fuller
list_of_players.append(cb)

ss.append('//*[@id="button-SS"]')
ss.append('983040_16_1_03') #Amos
list_of_players.append(ss)

fs.append('//*[@id="button-FS"]')
fs.append('983040_05_1_11') #Jackson
list_of_players.append(fs)

k.append('//*[@id="button-K"]')
k.append('983040_10_1_15') #Gould
k.append('983040_10_1_25') #Sparkey
list_of_players.append(k)

rs.append('//*[@id="button-KR"]/a')
rs.append('983040_09_1_04') #Cohen
list_of_players.append(rs)

p.append('//*[@id="button-P"]')
p.append('983040_12_1_23')
list_of_players.append(p)

st.append('//*[@id="button-ST"]')
st.append('983040_15_1_19')
list_of_players.append(st)


# Loop forever reopening browser each time
# due to StaleElementReference error :(
voteCount = 0
while True:

	# Iterate through positions
	for i in range(0,len(list_of_players)):
		
		# Load up driver
		driver = webdriver.Chrome()
		driver.get("http://www.nfl.com/probowl/ballot?team=LAC")
		action = ActionChains(driver)
		time.sleep(3)

		# Change player position
		while(position_change(list_of_players[i][0])):
			time.sleep(.5)

		# Iterate through players
		player_count = 0
		for j in range(1, len(list_of_players[i])):

			# Grab actual 'player' web element
			player = driver.find_element_by_id(list_of_players[i][j])

			scroll_height = 0
			while(player_count < len(list_of_players[i]) - 1):

				#Scroll to at least 2000 pixels
				if(scroll_height > 2100):
						scroll_height = 0

				#Execute javascript scroll
				scroll_script = "window.scrollTo(0,{})".format(scroll_height)
				driver.execute_script(scroll_script)
				scroll_height += 100
				time.sleep(.5)

				#Player found
				if(player_vote(player)):
					print("Player ID Found: " + list_of_players[i][j])
					player_count += 1
					scroll_height = 0
					break

		# Submit the actual vote!
		time.sleep(.3)
		submit()
		time.sleep(1)
		driver.close()
		time.sleep(2)

	# Vote count for entire team
	voteCount += 1
	print("\n>>>>>>>>>> Number of votes: {} <<<<<<<<<<".format(voteCount))