import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


df = pd.read_csv("ab_test_click_data.csv")
print(df.head())
print(df.describe())
print(df.groupby("group")["click"].sum())

group_counts = df.groupby("group").size()
print(group_counts)

group_click_counts = df.groupby(["group","click"]).size()
group_click_counts.reset_index()

palette = {0:"yellow",1:"black"}
plt.figure(figsize=(10,6))
ax = sns.countplot(data=df,x='group',hue='click',palette=palette)
plt.title("Click Distribution in Experiemental and Control Groups")
plt.xlabel("Group")
plt.ylabel("Count")
plt.legend(title="Click",labels=["No","Yes"])
group_counts = df.groupby("group").size()
group_click_counts = df.groupby(["group","click"]).size().reset_index(name='count')
for p in ax.patches[:-2]:
    h = p.get_height()
    group = 'exp' if p.get_x() < 0.5 else "con"
    total = group_counts[group]
    percentage = 100 * h / total
    ax.text(p.get_x() + p.get_width() / 2.,h+20,f'{percentage:.1f}%',ha='center',color='black',fontsize=10)

plt.tight_layout()
plt.show()


alpha = 0.05
print("Alpha: significance level is:",alpha)
delta = 0.1
print("Delta: minimum detectable level is:",delta)


n_con = df[df["group"] == "con"].count().loc["group"]
n_exp = df[df["group"] == "exp"].count().loc["group"]
x_con = df.groupby("group")["click"].sum().loc["con"]
x_exp = df.groupby("group")["click"].sum().loc["exp"]
print("Number of Users in Control:",n_con)
print("Number of Clicks in Control:",x_con)
print("Number of Users in Experiemental:",n_exp)
print("Number of Clicks in Experiemental:",x_exp)


p_con_hat = x_con / n_con
p_exp_hat = x_exp / n_exp
print("Click Probability in Control Group:",p_con_hat)
print("Click Probabilty in Experiemental Group:",p_exp_hat)
p_pooled = (x_con + x_exp) / (n_con + n_exp)

pooled_variance = p_pooled *  (1 - p_pooled) * (1/n_con + 1/n_exp)
print("P Pooled is:",p_pooled)
print("Pooled Variance:",pooled_variance)

se = np.sqrt(pooled_variance)
print("Standard Error is:",se)
test_stat = (p_con_hat - p_exp_hat) / se
print("Test Statistic for 2-samples is:",test_stat)
z_crit = stats.norm.ppf(1 - alpha / 2)
print("Z Critical Value:",z_crit)


p_value = 2 *stats.norm.sf(abs(test_stat))
def is_statistical_significance(p_value,alpha):
    print(f"P-Value of the 2 samples Z-test:",round(p_value,3))
    if p_value < alpha:
        print("There is statistical significance.")
    else:
        print("There is no statistical significance.")

is_statistical_significance(p_value,alpha)


mu = 0 
sigma = 1
x = np.linspace(mu - 3 *sigma,mu + 3 * sigma,100)
y = stats.norm.pdf(x,mu,sigma)
plt.plot(x,y,label="standard normal Distribution")
plt.fill_between(x,y,where= (abs(x) > z_crit),color='red',alpha=0.5,label="Rejection Region")
plt.axvline(test_stat,color='green',linestyle='--',linewidth=1,label=f'Test Statistic = {test_stat:.2f}')
plt.axvline(z_crit,color='blue',linestyle='--',linewidth=1,label=f"Z Critical = {z_crit:.2f}")
plt.axvline(-z_crit,color='blue',linestyle='--',linewidth=1)
plt.xlabel("Z Value")
plt.ylabel("Probability Density")
plt.title("Gaussian Distribution with Rejection Region \n (A/B Testing for Lunar CTA Button)")
plt.legend()
plt.show()


ci = [round((p_exp_hat - p_con_hat) - z_crit*se,2),round((p_exp_hat - p_con_hat) + z_crit*se,2)]
print("Confidence Interval of the 2 Sample Z-Testis :",ci)

def is_practically_significant(delta,ci_95):
    lw = ci_95[0]
    uw = ci_95[1]
    if delta >= lw:
        print("We have Practical Significance.")
        return True

    else:
        print("We don't have Practical Significance.")
        return False

significance = is_practically_significant(delta,ci)