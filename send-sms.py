import boto3

# Cria o serviço com as suas credenciais da AWS #
client = boto3.client(
    service_name="sns",
    region_name='***REGIÃO DO SEU SERVIÇO***', 
    aws_access_key_id='***SUA ACCESS_KEY***', 
    aws_secret_access_key='***SUA SECRET_KEY***'
)

# Envia o SMS para o número desejado #
client.publish(
    PhoneNumber="+5551999999999",
    Message="Olá Pycodebr :)"
)