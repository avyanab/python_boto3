import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text='This lab is teaching me how to code in AWS',
        SourceLanguageCode='en',
        TargetLanguageCode='es'
    )
    print(response) # this code is inside the function and will print the contents of the variable 'response'

def main():
    translate_text()
    
if __name__=="__main__":
    main()