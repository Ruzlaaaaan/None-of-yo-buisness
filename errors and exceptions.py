try:
    f=open("data.txt")
except Exception as e:
    print("Error:", e)
finally:
    print("File handling attempted")