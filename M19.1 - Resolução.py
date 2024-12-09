import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st

custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="ticks", rc=custom_params)

def multiselect_filter(relatorio, col, selecionados):
    if 'all' in selecionados:
        return relatorio
    else:
        return relatorio[relatorio[col].isin(selecionados)].reset_index(drop=True)


def main():
    st.set_page_config(page_title = 'Telemarketing analisys', 
        layout = 'wide',
        initial_sidebar_state = 'expanded'
    )
    
    st.write('# Telemarketing analisys')
    st.markdown("---")

    bank_raw = pd.read_csv('./dados/bank-full.csv', sep=';')
    bank = bank_raw.copy()

    st.write('## Antes dos filtros')
    st.write(bank_raw.head()) 

    with st.sidebar.form(key='my form'):

        # idades
        max_age = int(bank.age.max())
        min_age = int(bank.age.min())
        st.write('## Filtre por idade')
        idades = st.slider(label = 'Idade',
                            min_value = min_age,
                            max_value = max_age,
                            value = (min_age, max_age),
                            step = 1)


        # trabalhos
        jobs_list = bank.job.unique().tolist()
        jobs_list.append('all')

        st.write('## Filtre por trabalho')
        jobs_selected = st.multiselect('Profissões', 
                                            jobs_list,
                                            ['all'])

        bank = bank[(bank['age']>=idades[0]) & (bank['age']<=idades[1])]
        bank = multiselect_filter(bank, 'job', jobs_selected)
        
        submit_button = st.form_submit_button(label='Aplicar') 
        
    #apos os filtros
    st.write('## Apos os filtros')
    st.write(bank.head())
    st.markdown('---')


    # PLOTS    
    fig, ax = plt.subplots(1, 2, figsize = (15,7))

    bank_raw_pct = bank_raw.y.value_counts(normalize=True).to_frame()*100
    bank_raw_pct = bank_raw_pct.sort_index()
    sns.barplot(x = bank_raw_pct.index, 
                y = 'proportion',
                data = bank_raw_pct, 
                ax = ax[0])
    ax[0].bar_label(ax[0].containers[0])
    ax[0].set_title('Dados brutos',
                     fontweight ="bold")
        
    try:
        bank_target_perc = bank.y.value_counts(normalize = True).to_frame()*100
        bank_target_perc = bank_target_perc.sort_index()
        sns.barplot(x = bank_target_perc.index, 
                    y = 'proportion',                         data = bank_target_perc, 
                    ax = ax[1])
        ax[1].bar_label(ax[1].containers[0])
        ax[1].set_title('Dados filtrados',
                            fontweight ="bold")
    except:
        st.error('Erro no filtro')
        
    st.write('## Proporção de aceite')

    st.pyplot(plt)

if __name__ == '__main__':
	main()