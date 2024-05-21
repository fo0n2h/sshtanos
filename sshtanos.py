import paramiko
import openai

# Configuration SSH
ssh_host = 'adresse_ip_du_serveur'
ssh_port = 22
ssh_user = 'nom_utilisateur'
ssh_key_path = '/chemin/vers/votre/cle_privee'

# Configuration OpenAI
openai.api_key = 'votre_cle_openai'

def execute_ssh_command(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, port=ssh_port, username=ssh_user, key_filename=ssh_key_path)
    
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    
    ssh.close()
    return output, error

def get_gpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Ou le modèle spécifique que tu utilises
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    while True:
        user_input = input("Posez une question ou donnez une commande : ")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        # Utiliser le modèle pour générer une commande ou une réponse
        gpt_prompt = f"L'utilisateur a demandé: {user_input}\nRépondez ou générez la commande SSH appropriée."
        gpt_response = get_gpt_response(gpt_prompt)
        
        print(f"GPT-3/4 Suggestion: {gpt_response}")
        
        if input("Voulez-vous exécuter cette commande ? (yes/no) ").lower() == 'yes':
            output, error = execute_ssh_command(gpt_response)
            if output:
                print("Sortie:")
                print(output)
            if error:
                print("Erreur:")
                print(error)

if __name__ == "__main__":
    main()
