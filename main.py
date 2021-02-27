''' 
Simple IP address calculator. The inputs are the IP and the subnet mask. 
The outputs are the IP subnet, the range of usable IPs and the IP broadcast.
'''

from tkinter import *
from tkinter import messagebox

def binary_to_decimal(value):
    
    #Converts an IP-formatted value from binary to decimal
    splitted = value.split('.')
    decimal_value = [''for x in splitted]

    IP_position = 0
    for byte in splitted:
        value = 0
        iterator = '76543210'
        for bit in range(8):
            if byte[bit] == '1':
                value += 2**int(iterator[bit])
        decimal_value[IP_position] = str(value)
        IP_position += 1
        
    return '.'.join(decimal_value)
   
def decimal_to_binary(value):
    
    #Converts an IP-formatted decimal value to binary.
    splitted = value.split('.')
    bin_value = ['' for x in splitted]
    IP_position = 0
    for x in splitted:
        decimal = int(x)
        
        iterator = '76543210'
        value = ['0','0','0','0','0','0','0','0']
        count = 0
        for i in range(8):
            
            divisor = int(iterator[i])
            if decimal / (2**divisor) >= 1:
                value[count] = '1'
                decimal = decimal - 2**divisor
            count +=1    
           
        conv_value = ''
        for bit in value:
            conv_value = conv_value + bit
        bin_value[IP_position] = conv_value
        IP_position += 1
    
    return  '.'.join(bin_value)


def processing():
    # Main processing function: Gathers the binary IP address and SM.
    # Then compare their value in an and logic operation, to obtaint
    # the IP subnet to finally it into decimal, lastly to obtain the whole subnet
    
    binary_sub_mask = decimal_to_binary(choice.get()) # getting the binary SM
    binary_IP = decimal_to_binary(entryIP.get())      # getting the binary IP
    
    # Starting a loop to apply the and operator on the two binary IPs to obtain the IP subnet
    pointer = 0
    bin_IP_subnet = ""
    while pointer < 35:
        if binary_IP[pointer] ==  binary_sub_mask[pointer]:
            if binary_IP[pointer] == '.':
                bin_IP_subnet += '.'
            elif binary_IP[pointer] == '0': 
                bin_IP_subnet += '0'
            else:
                bin_IP_subnet += '1'
        else:
            bin_IP_subnet += '0'
        pointer += 1
    
    #Convert the IP to decimal and calculate the subnet
    IP_subnet = binary_to_decimal(bin_IP_subnet)
    #Get the subnet list
    subnet = findSubnet(IP_subnet)
    return visualisation(subnet)

def visualisation(subnet):
    
    # Output visualisation on a new window
    IP_subnet = subnet[0]
    IP_broadcast = subnet[-1]
    if int(subnet[1][-1]) - int(subnet[0][-1]) < 2:
        first_usable = "No usable"
        last_usable = "No usable"
    else:
        first_usable = subnet[0][0:-1] + str(int(subnet[0][-1])+1)
        last_usable = subnet[1][0:-1] + str(int(subnet[1][-1]) -1)
    top = Toplevel()
    frame_one = LabelFrame(top,padx = 5, pady = 5)
    frame_one.grid(row = 0, column = 0,padx = 150, pady = 20)
    Label(frame_one,text = f"IP Subnet: {IP_subnet}").grid(row= 0, column = 0)
    frame_two = LabelFrame(top,padx = 5, pady = 5)
    frame_two.grid(row = 1, column = 0,padx = 300, pady = 40)
    Label(frame_two,text = f"Range usable IP addresses: {first_usable} - {last_usable}").grid(row= 0, column = 0)
    frame_three = LabelFrame(top, padx = 5, pady = 5)
    frame_three.grid(row = 2, column = 0,padx = 150, pady = 20)
    Label(frame_three,text = f"IP Broadcast: {IP_broadcast}").grid(row=0,column=0)

    
    
    
    
def processingSubMask():
    
    #Function that calculates the range of the subnet
    binary_sub_mask = decimal_to_binary(choice.get())
    splitted = binary_sub_mask
    bit_count = 0
    for byte in splitted:
        for bit in byte:
            if bit == '0':
                bit_count += 1
    return 2 ** bit_count
    
        
def findSubnet(IP_subnet):
    #Function that gets the IP subnet as input.
    
    #Calling the function to calculate the range of the subnet
    range_IP = processingSubMask()
    #List containing the first value of the subnet. 
    usable_IP = [IP_subnet]
    
    #Calculation to find the IP broadcast
    splitted = IP_subnet.split('.')
    fourth_byte = int(splitted[-1])
    third_byte = int(splitted[-2])
    second_byte = int(splitted[-3])
    first_byte = int(splitted[0])
    fourth_byte += range_IP -1
    while fourth_byte > 255:
        third_byte +=1
        fourth_byte -= 256
    
    while third_byte > 255:
        second_byte +=1
        third_byte -= 256 
    while second_byte > 255:
        first_byte +=1
        second_byte -= 256
    #IP broadcast contatenation
    last_usable = str(first_byte) + '.' + str(second_byte) +'.'+ str(third_byte)+'.' + str(fourth_byte)          
    usable_IP.append(last_usable)
    return usable_IP
        
    
    


def button_clear():
    entryIP.delete(0,END)
    entryIP.insert(0,'')
    
def cancel():
    to_cancel = entryIP.get()
    entryIP.delete(0,END)
    splitted = []
    for letter in to_cancel:
        splitted.append(letter)
    splitted.pop()
    new = "".join(splitted)
    entryIP.insert(0,new)

def button_click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))


def returning():
    #Validation IP
    splitted = entryIP.get().split('.')
    if len(splitted) != 4:
        messagebox.showerror("Value error","The IP inserted doesn't contain 32-bit. Please insert 32-bit IP address")
        return None 
    for byte in splitted:
        try:
            int(byte)
        except:
            messagebox.showerror("Value error","One or more components of the IP address inserted not int. Please insert a valid value")
            return None
        else:    
            if int(byte) < 0 or int(byte)> 255:
                messagebox.showerror("Value error","One or more components of the IP address inserted is not 8-bit. Please insert a valid value")
                return None
            
    processing()
                              
def button_click(number):
    current = entryIP.get()
    entryIP.delete(0,END)
    entryIP.insert(0,str(current) + str(number))            


    
SUBLIST = ['255.0.0.0',
           '255.128.0.0',
           '255.192.0.0',
           '255.224.0.0',
           '255.240.0.0',
           '255.248.0.0',
           '255.252.0.0',
           '255.254.0.0',
           '255.255.0.0',
           '255.255.128.0',
           '255.255.192.0',
           '255.255.224.0',
           '255.255.240.0',
           '255.255.248.0',
           '255.255.252.0',
           '255.255.254.0',
           '255.255.255.0',
           '255.255.255.128',
           '255.255.255.192',
           '255.255.255.224',
           '255.255.255.240',
           '255.255.255.248',
           '255.255.255.252',
           '255.255.255.254',]

root = Tk()
root.title("IP Calculator")
choice = StringVar()
choice.set(SUBLIST[0])
entryIP = Entry(root, width = 35,borderwidth = 5)
entryIP.insert(0,"Insert here the IP address")
entryIP.grid(row = 0, column = 0,columnspan = 3)
entrysubMask = OptionMenu(root,choice, *SUBLIST)
entrysubMask.grid(row = 1, column = 1, columnspan = 3)



#Button widgets definition:    
button_r = Button(root, text = "Send", padx = 40, pady = 20, command = returning)
button1 = Button(root, text = 1, padx = 40, pady=20,command = lambda: button_click(1))
button2 = Button(root, text = 2, padx = 40, pady=20,command = lambda: button_click(2))
button3 = Button(root, text = 3, padx = 40, pady=20,command = lambda: button_click(3))
button4 = Button(root, text = 4, padx = 40, pady=20,command = lambda: button_click(4))
button5 = Button(root, text = 5, padx = 40, pady=20,command = lambda: button_click(5))
button6 = Button(root, text = 6, padx = 40, pady=20,command = lambda: button_click(6))
button7 = Button(root, text = 7, padx = 40, pady=20,command = lambda: button_click(7))
button8 = Button(root, text = 8, padx = 40, pady=20,command = lambda: button_click(8))
button9 = Button(root, text = 9, padx = 40, pady=20,command = lambda: button_click(9))
button0 = Button(root, text = 0, padx = 40, pady=20,command = lambda: button_click(0))
buttondot = Button(root, text = '.', padx = 40, pady=20,command = lambda: button_click('.'))
buttonCancel = Button(root, text = "Cancel", padx = 40, pady = 20, command = cancel)
buttonClear = Button(root, text = "Clear All", padx = 70, pady = 20, command = button_clear)

#Put the buttons on the screen
buttonCancel.grid(row = 4, column = 3)
button_r.grid(row = 0, column = 3)
button1.grid(row = 4,column = 0)
button2.grid(row =  4, column =1)
button3.grid(row =  4, column =2)
button4.grid(row = 3 , column =0)
button5.grid(row =  3, column =1)
button6.grid(row =  3, column =2)
button7.grid(row = 2 , column =0)
button8.grid(row =  2, column =1)
button9.grid(row = 2 , column =2)
button0.grid(row =  5, column =0)
buttonClear.grid(row= 5, column = 1,columnspan = 2)
buttondot.grid(row = 2, column = 3)

if __name__ == '__main__':
    mainloop()
