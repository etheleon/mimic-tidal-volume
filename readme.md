# Background:

## Lower Tv decreases ARDS mortality

* Lower tidal volume (Tv) ventilation (4-8 ml/kg ideal body weight) has been shown to reduce Acute Respiratory Distress Syndrome (ARDS) mortality by 25%
* Recent guidelines strongly support the use of lower Tv  in patients with ARDS
* Several authors have suggested that all mechanically ventilated patients should receive lower Tv ventilation despite lack of rigorous supporting evidence
* Since determining ARDS status is challenging, ventilation clinical trials are using hypoxaemic status, alone, or in combination with a minimum positive end expiratory pressure (PEEP) as a surrogate to ARDS status

![respiratory-disease](https://raw.githubusercontent.com/kiendang/mimic-tidal-volume/master/img/chart.png)
The Acute Respiratory Distress Syndrome Network. N Engl J Med 2000;342:1301–1308


# Motivation and Aim

## Motivation for study in MIMIC

Use MIMIC data to add to the mounting evidence in support of using lower Tv in all mechanically ventilated patients
Assess extent that clinical practice has adopted the lower Tv recommendations.

## Hypothesis

Mechanical ventilation using lower Tidal Volume lowers mortality of ICU patients with hypoxaemic respiratory failure.

# Data - Cohort Selection

Inclusion criteria:

| Criteria                                        | value                                               |
| ---                                             | ---                                                 |
| Age                                             | >= 18 years old                                     |
| Ventilation Type                                | Invasive                                            |
| Duration on ventilator                          | >= 48 hours                                         |
| Ventilator mode                                 | Intermittent Mandatory Control and Assisted Control |
| Hypoxaemic patients, defined as PaO2/FiO2 ratio | <= 300                                              |
| Positive End Expiratory Pressure (PEEP)         | >= 5 cmH2O                                          |
| Timeframe                                       | 2008-2012                                           |

Exclusion criteria:

Ventilator mode: Spontaneous breathing modes


# Methods

Cox regression on in-hospital mortality
Covariates
    * Tv
    * gender
    * Oasis 
    * Elixhauser 
    * Total hours on ventilation

# Baseline characteristics of patient population by initial tidal volume of ideal body weight

![table1](https://raw.githubusercontent.com/kiendang/mimic-tidal-volume/master/img/table1.png)

# Discussion + Future Aims

Adherence to low Tv in clinical practice is challenging. 51% of patients with hypoxemic respiratory failure received tidal volumes greater than 8ml/kg IBW

![table2](https://raw.githubusercontent.com/kiendang/mimic-tidal-volume/master/img/table2.png)

![dl](https://raw.githubusercontent.com/kiendang/mimic-tidal-volume/master/img/dl.png)

Plan to
* Determine best time to switch patients from mandatory ventilation to spontaneous/pressure support mode
* Include other ICU datasets
* Exclude ARDS patients
* Tailor results presentation for maximum clinical practice impact (eg. include APACHE, time on ventilation, hypoxaemic scoring cutoffs, etc)


# Reference

1.  Tremblay LN, Slutsky AS. Ventilator-induced lung injury: from the bench to the bedside. Intensive Care Med 2006;32:24–33.

2. Phua J, Badia JR, Adhikari NK, Friedrich JO, Fowler RA, Singh JM, Scales DC, Stather DR, Li A, Jones A, Gattas DJ, Hallett D, Tomlinson G, Stewart TE, Ferguson ND. Has mortality from acute respiratory distress syndrome decreased over time?: A systematic review. Am J Respir Crit Care Med 2009;179:220–227.

3. Ventilation with lower tidal volumes as compared with traditional tidal volumes for acute lung injury and the acute respiratory distress syndrome. The Acute Respiratory Distress Syndrome Network. N Engl J Med 2000;342:1301–1308.

4. Needham DM, Davidson J, Cohen H, Hopkins RO, Weinert C, Wunsch H, Zawistowski C, Bemis-Dougherty A, Berney SC, Bienvenu OJ, Brady SL, Brodsky MB, Denehy L, Elliott D, Flatley C, Harabin AL, Jones C, Louis D, Meltzer W, Muldoon SR, Palmer JB, Perme C, Robinson M, Schmidt DM, Scruth E, Spill GR, Storey CP, Render M, Votto J, et al. Improving long-term outcomes after discharge from intensive care unit: report from a stakeholders' conference. Critical Care Medicine 2012;40:502–509.

5. Rhodes A, Evans LE, Alhazzani W, Levy MM, Antonelli M, Ferrer R, Kumar A, Sevransky JE, Sprung CL, Nunnally ME, Rochwerg B, Rubenfeld GD, Angus DC, Annane D, Beale RJ, Bellinghan GJ, Bernard GR, Chiche J-D, Coopersmith C, De Backer DP, French CJ, Fujishima S, Gerlach H, Hidalgo JL, Hollenberg SM, Jones AE, Karnad DR, Kleinpell RM, Koh Y, et al. Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock: 2016. Intensive Care Med, 14 ed. 2017;43:1–74.

6. The ADTF. Acute Respiratory Distress Syndrome The Berlin Definition. JAMA 2012;307:2526–2533.

7. Beards SC, Jackson A, Hunt L, Wood A, Frerk CM, Brear G, Edwards JD, Nightingale P. Interobserver variation in the chest radiograph component of the lung injury score. Anaesthesia 1995;50:928–932.

8. Figueroa-Casas JB, Brunner N, Dwivedi AK, Ayyappan AP. Accuracy of the chest radiograph to identify bilateral pulmonary infiltrates consistent with the diagnosis of acute respiratory distress syndrome using computed tomography as reference standard. Journal of Critical Care 2013;28:352–357.

9. Rubenfeld GD, Caldwell E, Granton J, Hudson LD, Matthay MA. Interobserver variability in applying a radiographic definition for ARDS. Chest 1999;116:1347–1353.

10. Bellani G, Laffey JG, Pham T, Fan E, Brochard L, Esteban A, Gattinoni L, van Haren F, Larsson A, McAuley DF, Ranieri M, Rubenfeld G, Thompson BT, Wrigge H, Slutsky AS, Pesenti A, LUNG SAFE Investigators and the ESICM Trials Group. Epidemiology, Patterns of Care, and Mortality for Patients With Acute Respiratory Distress Syndrome in Intensive Care Units in 50 Countries. JAMA 2016;315:788–800.

11. Fröhlich S, Murphy N, Doolan A, Ryan O, Boylan J. Acute respiratory distress syndrome: underrecognition by clinicians. Journal of Critical Care 2013;28:663–668.

12. McNamee JJ, Gillies MA, Barrett NA, Agus AM, Beale R, Bentley A, Bodenham A, Brett SJ, Brodie D, Finney SJ, Gordon AJ, Griffiths M, Harrison D, Jackson C, McDowell C, McNally C, Perkins GD, Tunnicliffe W, Vuylsteke A, Walsh TS, Wise MP, Young D, McAuley DF. pRotective vEntilation with veno-venouS lung assisT in respiratory failure: A protocol for a multicentre randomised controlled trial of extracorporeal carbon dioxide removal in patients with acute hypoxaemic respiratory failure. Journal of the Intensive Care Society 2016;18:159–169.

13. Steinberg KP, Kacmarek RM. Respiratory controversies in the critical care setting. Should tidal volume be 6 mL/kg predicted body weight in virtually all patients with acute respiratory failure? Respir Care 2007;52:556–64– discussion 565–7.

14. The LAS VEGAS study, Investigators for the PROVE Network, the Clinical Trial Network of the European Society of Anaesthesiology. Epidemiology, practice of ventilation and outcome for patients at increased risk of postoperative pulmonary complications. European Journal of Anaesthesiology 2017;1–16.doi:10.1097/EJA.0000000000000646.

15. Brochard L, Slutsky A, Pesenti A. Mechanical Ventilation to Minimize Progression of Lung Injury in Acute Respiratory Failure. Am J Respir Crit Care Med 2017;195:438–442.

16. Schultz MJ, Haitsma JJ, Slutsky AS, Gajic O. What tidal volumes should be used in patients without acute lung injury? Anesthesiology 2007;106:1226–1231.

17. Ferguson ND. Low Tidal Volumes for All? JAMA 2012;308:1689–1690.


