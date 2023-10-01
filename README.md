# Automated Robust First Peak Detection in a Time Signal using Computational Intelligence

## INTRODUCTION
Peak detection within signals holds a pivotal role across various signal processing applications. The identification of peaks within data carries substantial societal significance, encompassing scenarios such as 
sudden fluctuations in stock markets, heart rate monitoring, traffic analysis, fuel price monitoring, and more. While the identification of peaks in single-variable time series data is relatively straightforward, 
it is imperative to establish a standardized definition of a peak to eliminate subjectivity. This standardization enables the development of algorithms capable of identifying peaks within diverse time series 
datasets. Presently, existing peak detection algorithms exhibit limitations in terms of seamless operation, underscoring the need for a straightforward and effective peak detection algorithm tailored for noisy signal 
analysis. 

To maintain the broad applicability of such algorithms, several essential steps can be employed. These steps include 
the detection of all local maxima points, the application of intelligent techniques for manual peak verification, and the establishment of a peak detection methodology resilient to 
high and low-frequency noise.

The task of detecting peaks within a signal and precisely characterizing their positions, thresholds, magnitudes, 
widths, or locations stands as a fundamental function within data processing applications. One approach to tackle this challenge is to leverage the mathematical insight that the first 
derivative of a peak exhibits a zero-crossing precisely at the peak's maximum point. To detect the first peak in a timeseries signal, a practical strategy involves the utilization of 
scientific computation libraries such as SciPy, which is part of the Scientific Python ecosystem and builds upon NumPy 
functionalities.

In our research model, we harness the capabilities of Linear Regression and Support Vector Machine to perform noise reduction, ultimately enabling the accurate prediction 
of the initial peak within a given time signal. By integrating these ML-driven approaches into the domain of peak detection, our research seeks to provide a novel and effective 
solution to the challenges posed by noisy signals. Through this innovative approach, we aim to enhance the reliability and precision of peak detection, opening new avenues for its 
application in a multitude of fields and scenarios.

## PROJECT IMPLEMMENTATION
- Background Studies:
 The ability to identify and effectively work with signal peaks holds immense importance across a wide spectrum of 
fields, ranging from engineering to economics. These peaks serve as critical markers, delineating the highest and lowest 
points within a dataset of functional values. This capability is instrumental in determining the positions and magnitudes of 
key statistical values, thereby facilitating predictive analysis and informed decision-making.

- Software Engineering Workflow:
 We have implemented the whole process using Agile methodologies, where we first plan the whole processconsisting of different approaches, design the system, 
develop our algorithm and then evaluate and test the built system.

- Environment Setup:
 To commence our experimental work, the initial step involves setting up and executing the project on our local 
machine. This entails configuring the necessary environment. In opting for the Python scripting language, we aimed to 
develop an algorithm capable of generating the desired output. Python's extensive technological capabilities afford a 
rich array of libraries conducive to computational intelligence. Furthermore, Python's versatility is highlighted 
by its compatibility with various programming paradigms, encompassing object-oriented and functional approaches.

For proper execution, the machine necessitates an installation of Python 3.10 or a more recent version. Additionally, the installation of the Anaconda environment or 
the PyCharm community edition is recommended. These tools streamline package management and facilitate seamless deployment.

## Run the project
In order to run the project, first clone this repository into your system, then make sure you have python installed and the global path variable is updated.
Now run the foloowing commands:

```
pip install sklearn matplotlib numpy scipy pandas openpyxl
python -m tkinter
```

If this all run successfully then you can run the following command:

```
python main.py
```

You will see a window like below:

![opening_ui](https://github.com/Mostainahmed/computational_intelligence/assets/20146137/65ee8c14-eb8c-46ea-9496-2250f909f45a)

Now you can input row and column value from your data sheet from where you want to start your computation of first peak.

![started_processing_signal](https://github.com/Mostainahmed/computational_intelligence/assets/20146137/70406205-83b7-4d17-aaf0-e2f60834d93e)


After inputting the value you have to choose you data sheet from file explorer.

![choosing_file_from_explorer](https://github.com/Mostainahmed/computational_intelligence/assets/20146137/6d7ef7bb-1566-402e-a647-591a6442d29c)


If you input any invalid value the application will let you choose your data sheet and go forward

![trying_to_open_a_file_without_valid_input](https://github.com/Mostainahmed/computational_intelligence/assets/20146137/9dfc9575-b968-41fd-a23c-7cb781c3b674)

![invalid_input_warning](https://github.com/Mostainahmed/computational_intelligence/assets/20146137/a148d548-aabb-4c48-9948-769bfd1cf924)

After successfull processing after a while depending on the data set and the processing power of the computer, you can see the first peak drawn on the application:


![peak_detection_1_large_data](https://github.com/Mostainahmed/computational_intelligence/assets/20146137/95dbfefd-a1db-42ad-b3b1-1de6e9aae763)

![peak_detection_2_small_data](https://github.com/Mostainahmed/computational_intelligence/assets/20146137/c277b02d-544f-491b-aa54-cdda5cd35bf0)

![peak_detection_3_large_data](https://github.com/Mostainahmed/computational_intelligence/assets/20146137/e0ab76dd-13c9-4956-b73e-dc9ca2e7882a)

![peak_detection_4_small_data](https://github.com/Mostainahmed/computational_intelligence/assets/20146137/dc7636e6-a011-44b9-a9d7-b9e6f31fa121)


[Here, is the link for further details of this project](https://github.com/Mostainahmed/computational_intelligence/blob/main/T2_COMP_2023.pdf)
