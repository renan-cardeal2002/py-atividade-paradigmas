import re
import pandas as pd
import matplotlib.pyplot as plt

# ex 1
def validar_ip(ip):
    padrao_ip = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

    if padrao_ip.match(ip):
        octetos = [int(octeto) for octeto in ip.split('.')]
        if all(0 <= octeto <= 255 for octeto in octetos):
            return True
    return False

def exercicio1():
    arquivo_entrada = 'arquivos/ips.txt'
    arquivo_saida = 'arquivos/relatorio_ips.txt'

    ips_validos = []
    ips_invalidos = []

    with open(arquivo_entrada, 'r') as file:
        enderecos_ip = file.read().split()

        for ip in enderecos_ip:
            if validar_ip(ip):
                ips_validos.append(ip)
            else:
                ips_invalidos.append(ip)

    with open(arquivo_saida, 'w') as file:
        file.write('[Enderecos validos:] ' + ' '.join(ips_validos) + '\n')
        file.write('[Enderecos invalidos:] ' + ' '.join(ips_invalidos) + '\n')

# ex 2

def exercicio2():
    df = pd.read_csv("arquivos/spotify-2023.csv", encoding="ISO-8859-1")
    df.columns = df.columns.str.strip()

    try:
        df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
    except ValueError:
        print("Erro ao converter 'streams' para valores numéricos.")

    df_filtro_streams = df[df['streams'] >= 100000000]

    colunas_para_plotar = ['released_year', 'streams', 'danceability_%', 'valence_%', 'energy_%']
    df[colunas_para_plotar].plot()
    plt.title('Streams do ano')
    plt.xlabel('Índice')
    plt.ylabel('Valores')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()

# ex 3

def bytes_to_mb(bytes_size):
    return bytes_size / (1024 ** 2)

def calculate_percentage(used_space, total_space):
    return (used_space / total_space) * 100

def exercicio3(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    total_space_used = 0
    users_data = []

    for line in lines:
        username, used_space = line.split()
        used_space = int(used_space)

        used_space_mb = bytes_to_mb(used_space)

        total_space_used += used_space_mb

        users_data.append((username, used_space_mb))

    users_data.sort(key=lambda x: x[1], reverse=True)

    with open(output_file, 'w') as report_file:
        report_file.write("ACME Inc. Uso do espaco em disco pelos usuarios\n")
        report_file.write("-" * 70 + "\n")
        report_file.write("{:<5} {:<15} {:<15} {:<15}\n".format("Nr.", "Usuario", "Espaco utilizado", "% do uso"))
        report_file.write("-" * 70 + "\n")

        for i, (username, used_space_mb) in enumerate(users_data, start=1):
            percentage = calculate_percentage(used_space_mb, total_space_used)
            report_file.write("{:<5} {:<15} {:<15.2f} MB {:<15.2f}%\n".format(i, username, used_space_mb, percentage))

        report_file.write("\nEspaco total ocupado: {:.2f} MB\n".format(total_space_used))
        report_file.write("Espaco médio ocupado: {:.2f} MB\n".format(total_space_used / len(users_data)))

if __name__ == "__main__":
    exercicio1()
    exercicio2()
    exercicio3("arquivos/usuarios.txt", "arquivos/relatorio.txt")