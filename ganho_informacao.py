import pandas as pd
import math as mat
from typing import Union


def entropia(df_dados: pd.DataFrame, nom_col_classe: str) -> float:
    """
    Calcula a entropia de acordo com df_dados (DataFrame) e a classe. Use a função math.log com
    o log na base 2. Não esqueça de importar o módulo math.

    df_dados: Dados a serem considerados para o calculo da entropia
    nom_col_classe: nome da coluna (em df_dados) que representa a classe
    """
    # substitua os None/0 quando necessario para completar o código
    # ser_count_col armazena, para cada valor da classe, a sua quantidade
    ser_count_col = df_dados[nom_col_classe].value_counts()
    num_total = len(df_dados)
    entropia = 0

    # Navege em ser_count_col para fazer o calculo da entropia
    for val_atr, count_atr in ser_count_col.items():
        # altere os valores de val_prob e entropia para o calculo correto da mesma
        # val_prob deverá ser a proporção de instancias de uma determinada classe
        # caso tenha duvida sobre o iteritems (items) e value_counts, consulte o passo a passo do pandas

        # valor da porcetagem de cada rotulo para cada atributo
        porc = count_atr / num_total
        val_prob = -(porc * mat.log2(porc))  # -(Pn log2(Pn))
        entropia += val_prob

    #print(f"Entropia de {nom_col_classe}: {entropia:.3f}")
    return entropia


def ganho_informacao_condicional(
    df_dados: pd.DataFrame,
    val_entropia_y: float,
    nom_col_classe: str,
    nom_atributo: str,
    val_atributo: Union[int, float, str, bool],
) -> float:
    """
    Calcula o GI(Y|nom_atributo=val_atributo), ou seja,
    calcula o ganho de informação do atributo 'nom_atributo' quando ele assume o valor 'val_atributo'.
    O valor de Entropia(Y) já foi calculado e está armazenado em val_entropia_y.
    Dica: A entropia condicional pode ser calculada filtrando o DataFrame df_dados.

    df_dados: Dataframe com os dados a serem analisados.
    val_entropia_y: Entropia(Y) (ver slides)
    nom_col_classe: nome da coluna que representa a classe
    nom_atributo: atributo a ser calculado o ganho de informação
    val_atributo: valor do atributo a ser considerado para este calculo. Uso do Union na dia do tipo:
                  o valor pode ser qualquer tipo primitivo (boolean, int, float ou str)
    """
    # substitua os "None"/0 quando necessario para completar o código
    # .em df_dados_filtrado, filtre o df_dados da forma correta - pensando quais
    # elementos considerar na entropia condicional Entropia(Y|nom_atributo=val_atributo).
    df_dados_filtrado = df_dados[df_dados[nom_atributo] == val_atributo]
    
    
    # use df_dados_filtrado para obter o valor de Entropia(Y|nom_atributo=val_atributo)
    val_ent_condicional = entropia(df_dados_filtrado, nom_col_classe)   
    
    # use val_ent_condicional para calcular o GI(Y|nom_atributo=val_atributo)
    val_gi = val_entropia_y - val_ent_condicional

    # para testes:
    #print(df_dados_filtrado[nom_col_classe].value_counts())
    print(f"GI({nom_col_classe}| {nom_atributo}={val_atributo}) = {val_gi}")

    return val_gi


def ganho_informacao(
    df_dados: pd.DataFrame, nom_col_classe: str, nom_atributo: str
) -> float:
    """
    Calcula GI(Y| nom_atributo), ou seja, o ganho de informação do atributo nom_atributo.

    df_dados: DataFrame com os dados a serem analisados.
    nom_col_classe: nome da coluna que representa a classe
    nom_atributo: atributo a ser calculado o ganho de informação
    val_atributo: valor do atributo a ser considerado para este calculo
    """
    # Muito similar ao codigo da entropia, mas aqui você deverá navegar sobre
    # os possiveis valores do atributo nom_atributo para calcular o infoGain
    # (usando a função ganho_informacao_condicional)
    # substitua os "None"/0 quando necessario para completar o código

    # atenção nessa linha abaixo, qual é o valor que temos que colocar em None?
    # o que precisamos contabilizar dessa vez?
    # A quantidade de vez que um atributo ("nom_atributo") se repete na amostra
    ser_count_col = df_dados[nom_atributo].value_counts()
    print(ser_count_col)

    val_entropia_y = entropia(df_dados, nom_col_classe)

    num_total = len(df_dados)
    
    val_info_gain = 0
    
    for val_atr, count_atr in ser_count_col.items():
        # val_prob * GI(nom_col_classe|val_atr = nom_atributo)
        val_prob = count_atr / num_total
        val_info_gain += val_prob * (ganho_informacao_condicional(df_dados, val_entropia_y, nom_col_classe, nom_atributo, val_atr))

        print(f"-> GI({nom_col_classe}| {nom_atributo}={val_atr}) = {val_info_gain}")

    return val_info_gain
