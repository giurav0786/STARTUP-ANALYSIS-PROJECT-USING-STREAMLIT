import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df  = pd.read_csv('clean_data1.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] =  df['date'].dt.year  
st.set_page_config(layout='wide',page_title='Startup Analysis')

def load_investors(investor):
    st.title(investor)
    st.sidebar.title('Start Funding Analysis')
    #load the recent 5 investments of the investors
    last5_df= df[df['investor'].str.contains(investor)].head()[['date','startup','verticle',  'city', 'inv_type', 'amount' ]]
    st.subheader('MOST RECENT INVESTMENTS')
    st.dataframe(last5_df)
    col1,cl2 = st.columns(2)
    with cl2:
        #Biggest investments
        big_series = df[df['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)
        st.subheader('TOP BIGGEST INVESTMENTS')
        # st.dataframe(big_series)
        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)
    with cl2:
        st.subheader('Top 10 SECTORS INVESTED  ')
        vaeticale_series = df[df['investor'].str.contains(investor)].groupby('verticle')['amount'].sum().sort_values(ascending=False).head(10)
        fig1, ax1 = plt.subplots()
        ax1.pie(vaeticale_series,labels=vaeticale_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)

    with cl2:
        st.subheader(' TOP 5 INVESTMENTS TYPE')
        stage_series = df[df['investor'].str.contains(investor)].groupby('inv_type')['amount'].sum().sort_values(ascending=False).head(5)
        fig2, ax2 = plt.subplots()
        ax2.pie(stage_series,labels=stage_series.index,autopct="%0.01f%%")
        st.pyplot(fig2)

    with col1:  
        year_series = df[df['investor'].str.contains(investor)].groupby('year')['amount'].sum()
        st.subheader(' YOY INVESTMENT (GRAPH)')
        fig4, ax4 = plt.subplots()
        ax4.plot(year_series.index,year_series.values)
        st.pyplot(fig4)
        st.subheader('TOP YOY INVESTMENT')
        st.dataframe(year_series.sort_values(ascending=False))

    with col1:
        st.subheader('TOP 10 INVESTMENTS IN CITY')
        city_series = df[df['investor'].str.contains(investor)].groupby('city')['amount'].sum().sort_values(ascending=False).head(10)
        fig3, ax3 = plt.subplots()
        ax3.pie(city_series,labels=city_series.index,autopct="%0.01f%%")
        st.pyplot(fig3)
    
#==============================================================================================================================================

def load_overall_ana():
    st.title('OverAll Analysis')
    # Total Invested Amount
    total = round(df['amount'].sum())
    # Maximum Funding
    max_fund = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # avg Ticket Size
    avg_funding =df.groupby('startup')['amount'].sum().mean() 
    # total funded Startups
    num_startups = df['startup'].nunique()


    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Total :',str(total) + '  crores')
    with col2:
        st.metric('Max :',str(max_fund) + '  crores')
    with col3:
        st.metric('Average :',str(round(avg_funding)) + '  crores')
    with col4:
        st.metric('Funded StartUp :',str(round(num_startups)) + '  crores')
    
    
    st.header('Top Sectors')
    top_sector = df.groupby(['verticle'])['amount'].sum().sort_values(ascending=False).head(10)
    fig3, ax3 = plt.subplots()
    ax3.bar(top_sector.index,top_sector.values)
    plt.xticks(rotation=90)
    st.pyplot(fig3)    

    st.header('Year Wise OverAll Investment')

    year_wise = df.groupby(['year'])['amount'].sum().sort_values(ascending=False)
    fig4, ax4 = plt.subplots()
    ax4.pie(year_wise,labels=year_wise.index,autopct="%0.01f%%")
    st.pyplot(fig4)

    st.header('Top 10 Investment Type Funded')

    inv_type = df.groupby(['inv_type'])['amount'].sum().sort_values(ascending=False).head(10)
    fig2, ax2 = plt.subplots()
    ax2.bar(inv_type.index,inv_type.values)
    plt.xticks(rotation=90)
    st.pyplot(fig2)

    st.header('Top 10 Cities Type Funded')
    top_city = df.groupby(['city'])['amount'].sum().sort_values(ascending=False).head(10)

    fig1, ax1 = plt.subplots()
    ax1.pie(top_city,labels=top_city.index,autopct="%0.01f%%")
    # plt.xticks(rotation=90)
    st.pyplot(fig1)   


    st.header('Top 10 Investors')
    top_inves =    df.groupby(['investor'])['amount'].sum().sort_values(ascending=False).head(10)
    fig5, ax5 = plt.subplots()
    ax5.pie(top_inves,labels=top_inves.index,autopct="%0.01f%%")
    # plt.xticks(rotation=90)
    st.pyplot(fig5) 

    st.header('Top 10 Investors')
    top_inves =    df.groupby(['investor'])['amount'].sum().sort_values(ascending=False).head(10)
    fig5, ax5 = plt.subplots()
    ax5.pie(top_inves,labels=top_inves.index,autopct="%0.01f%%")
    # plt.xticks(rotation=90)
    st.pyplot(fig5) 

def top_startups(name1):
    print(name1)
    cv =df[df['startup'].str.contains(name1)]['amount'].sum()
    # print(df['amount'].sort_values(ascending=False))
    print(cv)
    col1,col2 = st.columns(2)
    col3,col4 = st.columns(2)

    with col1:
        st.subheader('TOTAL STARTUP FUNDED')
        st.metric('Total :',str(cv) + '  crores')
    with col2:
        st.subheader('CITY WISE STARTUP FUNDED')
        cv1 =df[df['startup'].str.contains(name1)].groupby('city')['amount'].sum()
        fig6, ax6 = plt.subplots()
        ax6.pie(cv1,labels=cv1.index,autopct="%0.01f%%")
            # plt.xticks(rotation=90)
        st.pyplot(fig6)
    with col3:
        st.subheader('SERVISE WISE STARTUP FUNDED')
        cv1 =df[df['startup'].str.contains(name1)].groupby('verticle')['amount'].sum()
        fig6, ax6 = plt.subplots()
        ax6.pie(cv1,labels=cv1.index,autopct="%0.01f%%")
            # plt.xticks(rotation=90)
        st.pyplot(fig6)
    with col4:
        st.subheader('SUBSERVISE WISE STARTUP FUNDED')
        cv1 =df[df['startup'].str.contains(name1)].groupby('subverticle')['amount'].sum()
        fig6, ax6 = plt.subplots()
        ax6.pie(cv1,labels=cv1.index,autopct="%0.01f%%")
            # plt.xticks(rotation=90)
        st.pyplot(fig6)



#==============================================================================================================================================


option = st.sidebar.selectbox('Select one ', ['Overall Analysis', 'startUp', 'investor'])
if option == 'Overall Analysis' :
    btn0 = st.sidebar.button('Find StartUp Details')
    if btn0:
        load_overall_ana()


elif option == 'startUp':
    c = df[df['amount'] >0]['startup']
    x = []
    for startup in c:
        x.append(startup)
    x = str(x).replace("\\\\xe2\\\\x80\\\\x99", "").replace("\\\\xc2\\\\xa0", "").replace("\\\\xe2\\\\x80\\\\x99s", "").replace("\\\\xc3\\\\x98", "").replace("\\\\n\\\\n", "").replace("'", "").replace("\\\\\\\\xe2\\\\\\\\x80\\\\\\\\x99s", "").replace("''", "").replace("\\\\\\\\xc3\\\\\\\\x98", "").replace("\\\\\\\\xc2\\\\\\\\xa0", "").replace(".\\\\\\\\n\\\\\\\\n", "").replace("\\\\\\\\xe2\\\\\\\\x80\\\\\\\\x99", "").replace("'", "").replace("\\\\\\\\\\", "").replace(" https://www..in/", "wealthbucket").replace("\\\\\\\\n", "")
    df['startup']= df['startup'].str.replace("\\\\xe2\\\\x80\\\\x99", "").replace("\\\\xc2\\\\xa0", "").replace("\\\\xe2\\\\x80\\\\x99s", "").replace("\\\\xc3\\\\x98", "").replace("\\\\n\\\\n", "").replace("'", "").replace("\\\\\\\\xe2\\\\\\\\x80\\\\\\\\x99s", "").replace("''", "").replace("\\\\\\\\xc3\\\\\\\\x98", "").replace("\\\\\\\\xc2\\\\\\\\xa0", "").replace(".\\\\\\\\n\\\\\\\\n", "").replace("\\\\\\\\xe2\\\\\\\\x80\\\\\\\\x99", "").replace("'", "").replace("\\\\\\\\\\", "").replace(" https://www..in/", "wealthbucket").replace("\\\\\\\\n", "")

    x =x.strip().split(',')
    x =list(set(x))
    xx=pd.DataFrame(x, columns=["startups"])
    xx =list(xx['startups'].str.strip()) 

    investors_name =xx

    startup_name = st.sidebar.selectbox('Select StartUp', investors_name)
    btn1 = st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')
    if btn1:
        top_startups(startup_name)
else : 
    inves_name = st.sidebar.selectbox('Select Investors', sorted(set(df['investor'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investors Detail')
    if btn2:
        load_investors(inves_name)




