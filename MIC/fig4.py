import matplotlib.pyplot as plt
import pandas as pd

path = 'WHO.csv'
data = pd.read_csv(path)

if __name__ == '__main__':
    x = data[['Dentistry personnel density (per 10 000 population)']]
    y = data[['Years of life lost to injuries (%)']]

    plt.xlim([0, 17])
    plt.ylim([0, 41])
    plt.xticks(range(0, 17, 4))
    plt.yticks(range(0, 41, 10))

    plt.xlabel("Dentist Density (per 10,000) ")
    plt.ylabel("Life Lost to Injuries (% yrs)")

    plt.scatter(x, y, s=20)
    plt.show()

if __name__ == '__main__':
    x = data[['Children_per_woman']]
    y = data[['Life_expectancy_at_birth']]

    plt.xlim([0, 8])
    plt.ylim([30, 90])
    plt.xticks(range(0, 8, 2))
    plt.yticks(range(30, 100, 30))

    plt.xlabel("Children Per Woman")
    plt.ylabel("Life Expectancy (Years)")

    plt.scatter(x, y, s=20)
    plt.savefig('D.jpg')
    plt.show()

if __name__ == '__main__':
    x = data[['Number of physicians']]
    y = data[['Deaths due to HIV/AIDS (per 100 000 population per year)']]

    plt.xlim([0, 2*10**6])
    plt.ylim([0, 1800])
    plt.xticks(range(0, 3*10**5, 1*10**5))
    plt.yticks(range(0, 1800, 800))

    plt.xlabel("Number of Physicians")
    plt.ylabel("Deaths due to HIV/AIDS")

    plt.scatter(x, y, s=20)
    plt.savefig('E.jpg')
    plt.show()

if __name__ == '__main__':
    x = data[['Income_per_person']]
    y = data[['Prevalence of adults (&gt;=15 years) who are obese (%) female']]

    plt.xlim([0, 50000])
    plt.ylim([0, 76])
    plt.xticks(range(0, 50000, 20000))
    plt.yticks(range(0, 76, 25))

    plt.xlabel("Income / Person (Int$)")
    plt.ylabel("Adult (Female) Obesity (%)")

    plt.scatter(x, y, s=20)
    plt.savefig('F.jpg')
    plt.show()

if __name__ == '__main__':
    x = data[['Per capita government expenditure on health at average exchange rate (US$)']]
    y = data[['Measles immunization coverage among one-year-olds difference highest-lowest educational level of mother']]

    plt.xlim([0, 400])
    plt.ylim([-10, 60])
    plt.xticks(range(0, 400, 150))
    plt.yticks(range(-10, 60, 30))

    plt.xlabel("Health Exp. / Person (US$)")
    plt.ylabel("Measles Imm. Disparity (%)")

    plt.scatter(x, y, s=20)
    plt.savefig('G.jpg')
    plt.show()

if __name__ == '__main__':
    x = data[['Gross national income per capita (PPP international $)']]
    y = data[['Health_expenditure_per_person']]

    plt.xlim([0, 60000])
    plt.ylim([0, 7000])
    plt.xticks(range(0, 60000, 20000))
    plt.yticks(range(0, 8000, 2000))

    plt.xlabel("Gross Nat’l Inc / Person (Int$) ")
    plt.ylabel("Health Exp. / Person (Int $)")

    plt.scatter(x, y, s=20)
    plt.savefig('H.jpg')
    plt.show()
