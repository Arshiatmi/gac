import platform
import pyautogui
import clipboard


def checker():
	platform_data = platform.system() + platform.release()
	return platform_data.lower().strip()

def win10():
	platform_data = checker()
	if platform_data == "windows10":
		return True
	return False

def win8():
	platform_data = checker()
	if platform_data == "windows8":
		return True
	return False

def win7():
	platform_data = checker()
	if platform_data == "windows7":
		return True
	return False

def win():
	platform_data = checker()
	if platform_data.startswith("window"):
		return True
	return False

def lin():
	platform_data = checker()
	if platform_data.startswith("linux"):
		return True
	return False

def click(x,y):
	pyautogui.moveTo(x, y)
	pyautogui.click()

def doubleClick(x,y):
	pyautogui.moveTo(x, y)
	pyautogui.click()
	pyautogui.click()

def rightClick(x,y):
	pyautogui.moveTo(x, y)
	pyautogui.click(button='right')

def setClipboard(text):
	clipboard.copy(text)

def getClipboard():
	return clipboard.paste()