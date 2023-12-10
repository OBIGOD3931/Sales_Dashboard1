import pandas as pd 
import plotly.express as px 
import streamlit as st 


st.set_page_config(page_title="Sales Dashboard",
                    page_icon=":bar_chart:", 
                    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("CHM2403_Assignment 2_Part B_Dashboard_file.csv")
    return df

df = load_data()

# SIDEBAR
st.sidebar.header("Please filter here:")
product = st.sidebar.multiselect(
    "Select product:",
    options=df["Product"].unique(),
    default=df["Product"].unique()

)

segment = st.sidebar.multiselect(
    "Select segment:",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()

)

country = st.sidebar.multiselect(
    "Select country:",
    options=df["Country"].unique(),
    default=df["Country"].unique()

)

date = st.sidebar.multiselect(
    "Select date:",
    options=df["Date"].sort_values().unique(),
    default=df["Date"].sort_values().unique()
)

df_selection = df.query(
    "Product == @product & Segment ==@segment & Country == @country & Date == @date"
)

st.dataframe(df_selection)

# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI's

my_list = df_selection.columns

total_unit_sold = int(df_selection["Units Sold"].sum())
total_sales = int(df_selection[my_list[8]].sum())
total_profit = int(df_selection["Profit"].sum())
total_diccount = int(df_selection[my_list[7]].sum())
total_budget = int(df_selection["Budget"].sum())
average_unit_sold = round(df_selection["Units Sold"].mean(), 2)
average_sales = round(df_selection[my_list[8]].mean(), 2)



#average_rating = round(df_selection["Rating"].mean(), 1)
#star_rating = ":star:" * int(round(average_rating, 0))
#average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

column_1, column_2, column_3, column_4, column_5, column_6, column_7 = st.columns(7)
with column_1:
    st.subheader("Total Units Sold:")
    st.subheader(f"{total_unit_sold:,}")

with column_2:
    st.subheader("Total Sales:")
    st.subheader(f"€ {total_sales}")

with column_3:
    st.subheader("Total Profit:")
    st.subheader(f"€ {total_profit}")

#with column_4:
    st.subheader("Total Discount:")
    st.subheader(f"€ {total_diccount}")

with column_5:
    st.subheader("Total Budget:")
    st.subheader(f"€ {total_budget}")

with column_6:
    st.subheader("Average Units Sold:")
    st.subheader(f"€ {average_unit_sold}")

with column_7:
    st.subheader("Average Sales:")
    st.subheader(f"€ {average_sales}")

st.markdown("""---""")

my_list = df_selection.columns

# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product = df_selection.groupby(by=["Product"])[[my_list[8]]].sum().sort_values(by=my_list[8])
fig_product_sales = px.bar(
    sales_by_product,
    x=my_list[8],
    y=sales_by_product.index,
    orientation="h",
    title="<b>Sales by Product Bar Chart</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# SALES BY PRODUCT LINE [PIE CHART]
fig_pie_product = px.pie(sales_by_product, names=sales_by_product.index, values=my_list[8], title='Sales by Product Pie Chart')

# Display the charts in Streamlit
#st.plotly_chart(fig_product_sales)
#st.plotly_chart(fig_pie_product)


# SALES BY SEGMENT LINE [BAR CHART]
sales_by_segment = df_selection.groupby(by=["Segment"])[[my_list[8]]].sum().sort_values(by=my_list[8])
fig_segment_sales = px.bar(
    sales_by_segment,
    x=my_list[8],
    y=sales_by_segment.index,
    orientation="h",
    title="<b>Sales by Segment Bar Chart</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_segment),
    template="plotly_white",
)
fig_segment_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# SALES BY PRODUCT LINE [PIE CHART]
fig_pie_segment = px.pie(sales_by_segment, names=sales_by_segment.index, values=my_list[8], title='Sales by Segment Pie Chart')

# Display the charts in Streamlit
#st.plotly_chart(fig_segment_sales)
#st.plotly_chart(fig_pie_segment)

# SALES BY COUNTRY LINE [BAR CHART]
sales_by_country = df_selection.groupby(by=["Country"])[[my_list[8]]].sum().sort_values(by=my_list[8])
fig_country_sales = px.bar(
    sales_by_country,
    x=my_list[8],
    y=sales_by_country.index,
    orientation="h",
    title="<b>Sales by Country Bar Chart</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_country),
    template="plotly_white",
)
fig_country_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# SALES BY COUNTRY LINE [PIE CHART]
fig_pie_country = px.pie(sales_by_country, names=sales_by_country.index, values=my_list[8], title='Sales by Country Pie Chart')

# Display the charts in Streamlit
#st.plotly_chart(fig_country_sales)
#st.plotly_chart(fig_pie_country)


left_column, mid_column, right_column = st.columns(3, gap = "small")
left_column.plotly_chart(fig_product_sales, use_container_width=True)
mid_column.plotly_chart(fig_pie_product, use_container_width=True)
right_column.plotly_chart(fig_segment_sales, use_container_width=True)


left_column1, mid_column1, right_column1 = st.columns(3, gap = "small")
left_column1.plotly_chart(fig_pie_segment, use_container_width=True)
mid_column1.plotly_chart(fig_country_sales, use_container_width=True)
right_column1.plotly_chart(fig_pie_country, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
