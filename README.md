# **SIMULATION OF SPREAD OF VIRUS USING SIR MODEL**

# Contents

- [Overview](#overview)
- [Objective](#objective)
- [Methods and Materials](#methods-and-materials)
  - [S.I.R Model for prediction](#sir-model-for-prediction)
- [Outputs of the model](#outputs-of-the-model)
  - [Demo output of SIR model](#demo-output-of-sir-model)
  - [User defined output of SIR model](#user-defined-output-of-sir-model)
- [Comparison of different viruses](#comparison-of-different-viruses)
  - [Swine flu VS Ebola virus](#swine-flu-vs-ebola-virus)
  - [Corona VS Ebola virus](#corona-vs-ebola-virus)
  - [Corona VS Swine flu virus](#corona-vs-swine-flu-virus)
- [India's Situation on COVID-19 virus](#india's-situation-on-covid19-virus)
- [Conclusion](#conclusion)
- [References](#references)

## Overview

In this Project we are going to discuss on getting an idea about the Virus spread and its effect on the number of People and the ratio of Recovery also whether the Spread of Virus Leads to the Global Pandemic or not and finally on the difference of effectiveness with compared to different virus. We are going to predict it using **SIR MODEL** and in that we will provide a customized rate of Data and from that we can judge that how many people will get infected or how many are susceptible and recovered and what's the rate of increase by the future prediction and even we can compare with customized rate of data as well.

## Objective

The objective of making this model is done by taking consideration of the present scenario. The World Health Organization (WHO) has declared the coronavirus disease 2019 (COVID-19) a pandemic. A global coordinated effort is needed to stop the further spread of the virus. A pandemic is defined as "occurring over a wide geographic area and affecting an exceptionally high proportion of the population." The last pandemic reported in the world was the H1N1 flu pandemic in 2009.

On 31 December 2019, a cluster of cases of pneumonia of unknown cause, in the city of Wuhan, Hubei province in China, was reported to the World Health Organization. In January 2020, a previously unknown new virus was identified, subsequently named the 2019 novel coronavirus, and samples obtained from cases and analysis of the virus' genetics indicated that this was the cause of the outbreak. This novel coronavirus was named Coronavirus Disease 2019 (COVID-19) by WHO in February 2020. The virus is referred to as SARS-CoV-2 and the associated disease is COVID-19.

The best way to prevent and slow down transmission is to be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol-based rub frequently and not touching your face. Thus, this model helps us in predicting the time period where the spread of the virus is at its peak so that the precautious could be taken in advance to control the spread of viruses to a larger extent. Also, the study of this model suggests that that by manipulating with certain factors we can get a control over the transmission of viruses.

## Methods and Materials

### S.I.R Model for prediction

The S.I.R. (Susceptible, Infected/Infective and Recovered/Removed) Model is used in epidemiology to show analysis and relation between the number of people susceptible to a disease, currently with infection and people who have recovered or died at a given date or time from the total population.

This study focuses on the application of S.I.R models and statistical analysis to understand the spread viruses over a fixed number of populations. The data used for the graphical analysis was generated from the World Health Organization (WHO). The assumptions of the S.I.R model are:

- The diseases spread or outbreak is severe.
- The total population (N) is constant.
- II. Any individual in the population has an equal probability of contracting receiving the viruses.
- III. The number of people leaving a certain category is equal to the number of people joining a new category (i.e., the number of people leaving the susceptibility category is equivalent to the number of people joining the infected category).
- IV. The rate of recovery is faster than the time scale of birth and death
- V. There is homogenous mixing of population whereby each individual encounter contacts with similar people in ratio to each category
- VI. Everyone who gets infected is removed from the population either through recovery or death.

This can be represented mathematically below:
![image](https://user-images.githubusercontent.com/73428876/220174085-d4f3b164-526e-49a6-a15d-739ba5877b62.png)


Here it is assumed that total population N is fixed (No birth or deaths).

Therefore**, N = S + I + R.**

Here S= number of susceptible people.

- I=number of infected people.
- R= number of recovered people.
- N: total population

These variables change with respect to particular time so we have to define variables with respect to time.

> _**N = S (t) + I (t) + R (t)**_

- S(t): number of people susceptible on time(t).
- I(t): number of people infected on time(t).
- R(t): number of people recovered on time(t).

A two-dimensional system of three autonomous differential equations with state variables is given as:
![image](https://user-images.githubusercontent.com/73428876/220174472-3869e66b-ae1c-421c-8fed-df51e1c71fe5.png)

In the above Equation:
- **ds/dt** = the rate of change of the number of people susceptible to the disease with respect to time.
- **dI/dt** = the rate of change of the number of people infected with respect to time.
- **dR/dt** = the rate of change of the number of people recovered with respect to time.

![image](https://user-images.githubusercontent.com/73428876/220174567-577650ec-97b6-4915-ab74-23474c41452b.png)


>**[dS/dt = − β SI/N]** the only way an individual can leave the susceptible compartment is by coming into contact with somebody who has the infection and because of this, the righthand side (RHS) of equation is negative.

>**[ dI/dt= (β SI/N) – γI]** can be easily stated as the rate of flow of individual comes from the infected keeping total population constant and subtracting the recovered ones.

>**[dR/dt = γI]** the transition rate form is assumed to be proportional to the number of infectious individuals which is _γI_.

To calculate we need to define one or more parameter.
D=duration of disease for those recovered (time taken for recovery)

This leads to Between _I_ and _R_, this is equivalent to assuming that the probability of an infectious individual recovering in any time interval _dt_ is simply _γdt_. If an individual is infectious for an average time period _D_, then **γ = 1/D**. This is also equivalent to the assumption that the length of time spent by an individual in the infectious state is a random variable with an exponential distribution.

> **Basic Reproductive ratio** ( **R0= β/**  **γ** )

When R0 ≤1, then I (t)decrease monotonically to zero as t →∞

Thus, the infection would peter out and the spread of the virus will stop and thus its spread would not result in an epidemic.

When  ![](RackMultipart20230220-1-f7dams_html_d07ea436582878ce.gif), each person who gets the disease will infect more than one person, so the epidemic will spread.

As a quick recap, take a look at the variables we defined:

- N: total population
- S(t): number of people susceptible on day t
- I(t): number of people infected on day t
- R(t): number of people recovered on day t
- β: expected amount of people an infected person infects per day
- D: number of days an infected person has and can spread the disease
- γ: the proportion of infected recovering per day (γ = 1/D)
- R₀: the total number of people an infected person infects (R₀ = β / γ)

## Outputs of the model

#### Demo output of SIR model

<img src="https://user-images.githubusercontent.com/73428876/220176694-49795576-8dec-4de6-a197-448b98fbf457.png" width="50%" height="30%">

The above graph shows the demo output of SIR model on daily basis for the infected, susceptible and recovered number of people. From this graph, we can state that initially the no of susceptible people is very high due to the less spreading of the virus but with time, it goes on decreasing as the infected no of people increases. After certain period of time, the recovered no of people increases as they are immune to the virus and have recovered and thus would not be susceptible to the infected anymore.

<img src="https://user-images.githubusercontent.com/73428876/220175199-2c29a7ff-adfb-4f82-8b2e-8ca98324a698.png" width="50%" height="30%">

_The above graph shows the cumulative representation of SIR model._

#### User defined output of SIR model
<img src="https://user-images.githubusercontent.com/73428876/220175276-0831fb0d-5baf-4863-886d-91c04eb2101d.png" width="50%" height="30%">

_The above graph shows the output of the user defined SIR model on daily basis._

<img src="https://user-images.githubusercontent.com/73428876/220175468-c7720b05-7db8-4f8a-851c-6353e4fb60aa.png"  width="50%" height="30%">


_The above graph shows the output of the user defined SIR model on cumulative basis._

## Comparison of different viruses

#### Swine flu VS Ebola virus
<img src="https://user-images.githubusercontent.com/73428876/220175580-ddf8705d-2fcd-42cd-bdfe-ea18193ca7f8.png"  width="40%" height="20%">

> This graph shows that initially, the infected number of people was high in swine flu than Ebola virus. But after that, the cases decreased and in nearly 2-4 months, swine flu cases were not much but the spread of Ebola virus went on for several months. 

<img src="https://user-images.githubusercontent.com/73428876/220175614-ddaf5bfb-d502-45e8-9b6d-2c497da9457b.png"  width="40%" height="20%">

> This graph shows that initially, the infected number of people was high in swine flu than Ebola virus. But after that, the cases decreased and in nearly 2-4 months, swine flu cases were not much but the spread of Ebola virus went on for several months.

<img src="https://user-images.githubusercontent.com/73428876/220175614-ddaf5bfb-d502-45e8-9b6d-2c497da9457b.png"  width="40%" height="20%">

> The above graph shows that the death count of swine flu was very low and it went on for only like 3 months but the death count of Ebola virus kept on going high and low for like 16 months.

#### Corona VS Ebola virus

<img src="https://user-images.githubusercontent.com/73428876/220175695-e8ca2953-adb8-4e85-b24d-f1c811bb4414.png" width="40%" height="20%">

<img src="https://user-images.githubusercontent.com/73428876/220175855-cd41d1de-ab0d-4030-97be-abc16e3d93c7.png" width="40%" height="20%">

#### Corona VS Swine flu virus

<img src="https://user-images.githubusercontent.com/73428876/220175874-0363e841-8276-423b-8324-b0774abacb61.png" width="40%" height="20%">

<img src="https://user-images.githubusercontent.com/73428876/220175890-20107bd2-fb11-4f54-ae4b-8f8b6dae81f7.png" width="40%" height="20%">

## India's Situation on COVID-19 virus

<img src="https://user-images.githubusercontent.com/73428876/220175931-f8c503af-6df4-4bbc-be8f-0eba2431d863.png" width="60%" height="30%">

Above graph shows the cumulative plot of the number of confirmed covid19 cases in India.

<img src="https://user-images.githubusercontent.com/73428876/220175948-603da830-861d-49f1-b100-fdddccba09bc.png" width="60%" height="30%">

Above graph shows the cumulative plot of the number of people recovered from the infection due to Covi19 in India.

<img src="https://user-images.githubusercontent.com/73428876/220175958-f193a179-7bee-4d93-96f1-a16854470da0.png" width="60%" height="30%">

Above graph shows the cumulative plot of the deaths of the people due to Covi19 in India.

The above three graphs show the confirmed cases, recovery of people and deaths in India due to corona virus on cumulative basis. And we can see that the spread of virus, people's recovery and the deaths have gone high.

## Conclusion

The results obtained from modelling data can lead to differing perspectives and interpretations.

By using an SIR model, we were able to see the importance of modelling data. Further insight was gathered in the ways in which modelling can be used to predict the apparent spread of diseases in order to inform health care superficial of the necessary precautions that must be in place.

SIR models are suitable to describe the transmission of infectious diseases with lifelong immunity. A lot of continuous SIR models with various transmission rates have been formulated and studied. The global stability of the endemic equilibrium of the continuous SIR model has been investigated extensively and many sufficient conditions have been obtained.

The complicated dynamics of the simple SIR model reminds us that we cannot expect to have the global stability of the endemic equilibrium when R0\>1. If R0\>1 than we can say that it is confirmed pandemic globally and not stable condition.

The SIR model showed the general trend of the epidemic, however due to its limitations which eventually outweighed the advantages, the model did not precisely correspond to the real-life data, although they mostly illustrated similar correlation.


## References

- Atinuke, B., Micheal, B., &amp; Bagbe, A. (2019, May 31). Statistical Analysis of Ebola Virus Disease outbreak in Some West Africa Countries using S-I-R Model. Retrieved December 10, 2020, from [https://irispublishers.com/abba/fulltext/statistical-analysis-of-ebola-virus-disease-outbreak-in-some-west-africa-countries-using-s-i-r-model.ID.000540.php](https://irispublishers.com/abba/fulltext/statistical-analysis-of-ebola-virus-disease-outbreak-in-some-west-africa-countries-using-s-i-r-model.ID.000540.php)
- Kermack-McKendrick Model. (n.d.). Retrieved December 10, 2020, from [https://mathworld.wolfram.com/Kermack-McKendrickModel.html](https://mathworld.wolfram.com/Kermack-McKendrickModel.html)
- The SIR Model for Spread of Disease - The Differential Equation Model. (n.d.). Retrieved December 10, 2020, from [https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model](https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model)
- Bazett, D., 2020. The MATH Of Epidemics | Intro To The SIR Model. [video] Available at: \<https://www.youtube.com/watch?v=Qrp40ck3WpI\> [Accessed 10 December 2020].
