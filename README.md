**Project Portfolio: https://github.com/calebyhan/CalebHan** 

Approximating functions with taylor polynomials. Functions explored: sin(x), cos(x), tan⁻¹(x), eˣ, ln(x).

* Approximating Taylor Series and finding error
* Graphing difference in the polynomials in number of terms


## sin

$$\begin{align}
\sin(x) & = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!} - ... \\
& = \sum_{n=1}^{\infty}{(-1)^n \frac{x^{2n + 1}}{(2n + 1)!}} \\
\end{align}$$

```
# approximating cos(π/2)
1 terms: Approx = 1.5707963267948966, Exact = 1.0, Error = 0.5707963267948966
2 terms: Approx = 0.9248322292886504, Exact = 1.0, Error = 0.07516777071134961
3 terms: Approx = 1.0045248555348174, Exact = 1.0, Error = 0.004524855534817407
4 terms: Approx = 0.9998431013994987, Exact = 1.0, Error = 0.00015689860050127624
5 terms: Approx = 1.0000035425842861, Exact = 1.0, Error = 3.542584286142514e-06
6 terms: Approx = 0.999999943741051, Exact = 1.0, Error = 5.625894905492146e-08
7 terms: Approx = 1.0000000006627803, Exact = 1.0, Error = 6.627802751069112e-10
8 terms: Approx = 0.9999999999939768, Exact = 1.0, Error = 6.023181953196399e-12
9 terms: Approx = 1.0000000000000437, Exact = 1.0, Error = 4.374278717023117e-14
10 terms: Approx = 1.0, Exact = 1.0, Error = 0.0
```

![sin](https://cdn.discordapp.com/attachments/905301278647783428/1090421286490087424/image.png)


## cos

$$\begin{align}
\cos(x) & = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!} - ... \\
& = \sum_{n=0}^{\infty}{(-1)^n \frac{x^{2n}}{(2n)!}}\\
\end{align}$$

```
# approximating cos(π)
1 terms: Approx = 1.0, Exact = -1.0, Error = 2.0
2 terms: Approx = -3.934802200544679, Exact = -1.0, Error = 2.934802200544679
3 terms: Approx = 0.1239099258720886, Exact = -1.0, Error = 1.1239099258720886
4 terms: Approx = -1.2113528429825007, Exact = -1.0, Error = 0.21135284298250068
5 terms: Approx = -0.9760222126236076, Exact = -1.0, Error = 0.023977787376392445
6 terms: Approx = -1.0018291040136216, Exact = -1.0, Error = 0.0018291040136215742
7 terms: Approx = -0.9998995297042177, Exact = -1.0, Error = 0.0001004702957823067
8 terms: Approx = -1.0000041678091425, Exact = -1.0, Error = 4.16780914247461e-06
9 terms: Approx = -0.9999998647395555, Exact = -1.0, Error = 1.352604445115091e-07
10 terms: Approx = -1.0000000035290801, Exact = -1.0, Error = 3.5290801392307003e-09
11 terms: Approx = -0.9999999999243493, Exact = -1.0, Error = 7.565070792026063e-11
12 terms: Approx = -1.0000000000013565, Exact = -1.0, Error = 1.3564704914870163e-12
13 terms: Approx = -0.9999999999999796, Exact = -1.0, Error = 2.042810365310288e-14
14 terms: Approx = -1.0000000000000004, Exact = -1.0, Error = 4.440892098500626e-16
```

![cos](https://cdn.discordapp.com/attachments/905301278647783428/1090419150108774400/image.png)


## tan⁻¹

$$\begin{align}
\tan^{-1} & = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \frac{x^9}{9} - ... \\
& = \sum_{n=1}^{\infty}{(-1)^n \frac{x^{2n + 1}}{2n + 1}}\\
\end{align}$$

```
1 terms: Approx = 0.7853981633974483, Exact = 0.6657737500283538, Error = 0.11962441336909446
2 terms: Approx = 0.6239071390208868, Exact = 0.6657737500283538, Error = 0.041866611007467025
3 terms: Approx = 0.6836766087055121, Exact = 0.6657737500283538, Error = 0.01790285867715824
4 terms: Approx = 0.6573417416943445, Exact = 0.6657737500283538, Error = 0.008432008334009367
5 terms: Approx = 0.669976484996349, Exact = 0.6657737500283538, Error = 0.00420273496799517
6 terms: Approx = 0.6635997846389575, Exact = 0.6657737500283538, Error = 0.002173965389396293
7 terms: Approx = 0.6669281048746745, Exact = 0.6657737500283538, Error = 0.0011543548463206488
8 terms: Approx = 0.6651487729888134, Exact = 0.6657737500283538, Error = 0.000624977039540453
9 terms: Approx = 0.6661172271328406, Exact = 0.6657737500283538, Error = 0.00034347710448678903
10 terms: Approx = 0.6655827192124576, Exact = 0.6657737500283538, Error = 0.0001910308158962204
11 terms: Approx = 0.6658810294884848, Exact = 0.6657737500283538, Error = 0.00010727946013100453
12 terms: Approx = 0.6657130178236029, Exact = 0.6657737500283538, Error = 6.0732204750890695e-05
13 terms: Approx = 0.6658083648219643, Exact = 0.6657737500283538, Error = 3.4614793610443506e-05
14 terms: Approx = 0.6657539066532919, Exact = 0.6657737500283538, Error = 1.9843375061889823e-05
15 terms: Approx = 0.665785182462974, Exact = 0.6657737500283538, Error = 1.14324346202066e-05
16 terms: Approx = 0.6657671346480594, Exact = 0.6657737500283538, Error = 6.6153802944501905e-06
17 terms: Approx = 0.6657775927325269, Exact = 0.6657737500283538, Error = 3.842704173084854e-06
18 terms: Approx = 0.6657715102929481, Exact = 0.6657737500283538, Error = 2.2397354056957752e-06
19 terms: Approx = 0.6657750594391225, Exact = 0.6657737500283538, Error = 1.3094107687017242e-06
20 terms: Approx = 0.6657729824187026, Exact = 0.6657737500283538, Error = 7.676096511755048e-07
21 terms: Approx = 0.6657742011312411, Exact = 0.6657737500283538, Error = 4.5110288726668557e-07
22 terms: Approx = 0.6657734843338051, Exact = 0.6657737500283538, Error = 2.656945486956275e-07
23 terms: Approx = 0.665773906839092, Exact = 0.6657737500283538, Error = 1.5681073817219726e-07
24 terms: Approx = 0.6657736573069089, Exact = 0.6657737500283538, Error = 9.272144496641488e-08
25 terms: Approx = 0.6657738049482926, Exact = 0.6657737500283538, Error = 5.491993881889812e-08
26 terms: Approx = 0.6657737174471401, Exact = 0.6657737500283538, Error = 3.258121372695655e-08
27 terms: Approx = 0.6657737693854535, Exact = 0.6657737500283538, Error = 1.9357099700911817e-08
28 terms: Approx = 0.6657737385123147, Exact = 0.6657737500283538, Error = 1.1516039122305699e-08
29 terms: Approx = 0.6657737568882047, Exact = 0.6657737500283538, Error = 6.8598509095352256e-09
30 terms: Approx = 0.6657737459372751, Exact = 0.6657737500283538, Error = 4.091078698031936e-09
31 terms: Approx = 0.6657737524708809, Exact = 0.6657737500283538, Error = 2.442527069490552e-09
32 terms: Approx = 0.665773748568569, Exact = 0.6657737500283538, Error = 1.4597848485564668e-09
33 terms: Approx = 0.6657737509016453, Exact = 0.6657737500283538, Error = 8.732914391629265e-10
34 terms: Approx = 0.6657737495054465, Exact = 0.6657737500283538, Error = 5.229072730372764e-10
35 terms: Approx = 0.6657737503417285, Exact = 0.6657737500283538, Error = 3.1337465955516564e-10
36 terms: Approx = 0.665773749840399, Exact = 0.6657737500283538, Error = 1.8795476286470603e-10
37 terms: Approx = 0.6657737501411718, Exact = 0.6657737500283538, Error = 1.1281797718254438e-10
38 terms: Approx = 0.6657737499605876, Exact = 0.6657737500283538, Error = 6.776623706628015e-11
39 terms: Approx = 0.6657737500690877, Exact = 0.6657737500283538, Error = 4.073386072889207e-11
40 terms: Approx = 0.6657737500038537, Exact = 0.6657737500283538, Error = 2.4500068640520567e-11
41 terms: Approx = 0.6657737500430998, Exact = 0.6657737500283538, Error = 1.474598221307133e-11
42 terms: Approx = 0.6657737500194743, Exact = 0.6657737500283538, Error = 8.879563750952002e-12
43 terms: Approx = 0.6657737500337048, Exact = 0.6657737500283538, Error = 5.350941911785867e-12
44 terms: Approx = 0.6657737500251284, Exact = 0.6657737500283538, Error = 3.2254199311410048e-12
45 terms: Approx = 0.6657737500302998, Exact = 0.6657737500283538, Error = 1.9459989175629744e-12
46 terms: Approx = 0.66577375002718, Exact = 0.6657737500283538, Error = 1.173838803936178e-12
47 terms: Approx = 0.6657737500290631, Exact = 0.6657737500283538, Error = 7.093214904330125e-13
48 terms: Approx = 0.665773750027926, Exact = 0.6657737500283538, Error = 4.277689313880728e-13
49 terms: Approx = 0.665773750028613, Exact = 0.6657737500283538, Error = 2.5923707624997405e-13
50 terms: Approx = 0.6657737500281978, Exact = 0.6657737500283538, Error = 1.559863349598345e-13
51 terms: Approx = 0.6657737500284489, Exact = 0.6657737500283538, Error = 9.50350909079134e-14
52 terms: Approx = 0.665773750028297, Exact = 0.6657737500283538, Error = 5.684341886080802e-14
53 terms: Approx = 0.6657737500283889, Exact = 0.6657737500283538, Error = 3.5083047578154947e-14
54 terms: Approx = 0.6657737500283333, Exact = 0.6657737500283538, Error = 2.0539125955565396e-14
55 terms: Approx = 0.6657737500283669, Exact = 0.6657737500283538, Error = 1.3100631690576847e-14
56 terms: Approx = 0.6657737500283465, Exact = 0.6657737500283538, Error = 7.327471962526033e-15
57 terms: Approx = 0.6657737500283588, Exact = 0.6657737500283538, Error = 4.9960036108132044e-15
58 terms: Approx = 0.6657737500283514, Exact = 0.6657737500283538, Error = 2.4424906541753444e-15
59 terms: Approx = 0.6657737500283559, Exact = 0.6657737500283538, Error = 2.1094237467877974e-15
60 terms: Approx = 0.6657737500283532, Exact = 0.6657737500283538, Error = 6.661338147750939e-16
61 terms: Approx = 0.6657737500283548, Exact = 0.6657737500283538, Error = 9.992007221626409e-16
62 terms: Approx = 0.6657737500283538, Exact = 0.6657737500283538, Error = 0.0
```

![atan](https://cdn.discordapp.com/attachments/905301278647783428/1090423961910784100/image.png)


## eˣ

$$\begin{align}
{\rm e}^x & = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + ... \\
& = \sum_{n=0}^{\infty}{\frac{x^n}{n!}}\\
\end{align}$$

```
1 terms: Approx = 1.0, Exact = 7.3890560989306495, Error = 6.3890560989306495
2 terms: Approx = 3.0, Exact = 7.3890560989306495, Error = 4.3890560989306495
3 terms: Approx = 5.0, Exact = 7.3890560989306495, Error = 2.3890560989306495
4 terms: Approx = 6.333333333333333, Exact = 7.3890560989306495, Error = 1.0557227655973165
5 terms: Approx = 7.0, Exact = 7.3890560989306495, Error = 0.3890560989306495
6 terms: Approx = 7.266666666666667, Exact = 7.3890560989306495, Error = 0.12238943226398291
7 terms: Approx = 7.355555555555555, Exact = 7.3890560989306495, Error = 0.03350054337509434
8 terms: Approx = 7.3809523809523805, Exact = 7.3890560989306495, Error = 0.008103717978269032
9 terms: Approx = 7.387301587301587, Exact = 7.3890560989306495, Error = 0.001754511629062705
10 terms: Approx = 7.3887125220458545, Exact = 7.3890560989306495, Error = 0.0003435768847950271
11 terms: Approx = 7.388994708994708, Exact = 7.3890560989306495, Error = 6.138993594184683e-05
12 terms: Approx = 7.389046015712681, Exact = 7.3890560989306495, Error = 1.0083217968137603e-05
13 terms: Approx = 7.3890545668323435, Exact = 7.3890560989306495, Error = 1.532098306000762e-06
14 terms: Approx = 7.389055882389215, Exact = 7.3890560989306495, Error = 2.1654143456117936e-07
15 terms: Approx = 7.3890560703259105, Exact = 7.3890560989306495, Error = 2.860473902188687e-08
16 terms: Approx = 7.389056095384136, Exact = 7.3890560989306495, Error = 3.5465133052525744e-09
17 terms: Approx = 7.389056098516415, Exact = 7.3890560989306495, Error = 4.142348686286823e-10
18 terms: Approx = 7.389056098884918, Exact = 7.3890560989306495, Error = 4.573141865193975e-11
19 terms: Approx = 7.389056098925863, Exact = 7.3890560989306495, Error = 4.786393503763975e-12
20 terms: Approx = 7.3890560989301735, Exact = 7.3890560989306495, Error = 4.760636329592671e-13
21 terms: Approx = 7.389056098930604, Exact = 7.3890560989306495, Error = 4.529709940470639e-14
22 terms: Approx = 7.389056098930645, Exact = 7.3890560989306495, Error = 4.440892098500626e-15
23 terms: Approx = 7.389056098930649, Exact = 7.3890560989306495, Error = 8.881784197001252e-16
```

![e](https://cdn.discordapp.com/attachments/905301278647783428/1090431697222369370/image.png)

## ln

$$\begin{align}
\ln(x) & = x-1 - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3} - \frac{(x-1)^4}{4} + ... \\
& = \sum_{n=1}^{\infty}{(-1)^{n-1}\frac{(x-1)^n}{n}}\\
\end{align}$$

```
1 terms: Approx = 0, Exact = 0.4054651081081644, Error = 0.4054651081081644
2 terms: Approx = 0.5, Exact = 0.4054651081081644, Error = 0.09453489189183562
3 terms: Approx = 0.375, Exact = 0.4054651081081644, Error = 0.030465108108164385
4 terms: Approx = 0.4166666666666667, Exact = 0.4054651081081644, Error = 0.0112015585585023
5 terms: Approx = 0.4010416666666667, Exact = 0.4054651081081644, Error = 0.0044234414414977
6 terms: Approx = 0.40729166666666666, Exact = 0.4054651081081644, Error = 0.001826558558502278
7 terms: Approx = 0.4046875, Exact = 0.4054651081081644, Error = 0.0007776081081644071
8 terms: Approx = 0.40580357142857143, Exact = 0.4054651081081644, Error = 0.0003384633204070453
9 terms: Approx = 0.40531529017857143, Exact = 0.4054651081081644, Error = 0.0001498179295929547
10 terms: Approx = 0.4055323040674603, Exact = 0.4054651081081644, Error = 6.719595929594036e-05
11 terms: Approx = 0.4054346478174603, Exact = 0.4054651081081644, Error = 3.046029070408185e-05
12 terms: Approx = 0.4054790370220058, Exact = 0.4054651081081644, Error = 1.3928913841387836e-05
13 terms: Approx = 0.40545869196992246, Exact = 0.4054651081081644, Error = 6.416138241926994e-06
14 terms: Approx = 0.4054680819939609, Exact = 0.4054651081081644, Error = 2.973885796508924e-06
15 terms: Approx = 0.40546372233994304, Exact = 0.4054651081081644, Error = 1.3857682213402889e-06
16 terms: Approx = 0.4054657568451514, Exact = 0.4054651081081644, Error = 6.487369870189497e-07
17 terms: Approx = 0.405464803170835, Exact = 0.4054651081081644, Error = 3.0493732938730034e-07
18 terms: Approx = 0.4054652519587486, Exact = 0.4054651081081644, Error = 1.4385058422217156e-07
19 terms: Approx = 0.4054650400311227, Exact = 0.4054651081081644, Error = 6.807704167055562e-08
20 terms: Approx = 0.4054651404178929, Exact = 0.4054651081081644, Error = 3.2309728503765456e-08
21 terms: Approx = 0.4054650927341771, Exact = 0.4054651081081644, Error = 1.5373987305444814e-08
22 terms: Approx = 0.4054651154407084, Exact = 0.4054651081081644, Error = 7.332544016414033e-09
23 terms: Approx = 0.40546510460350027, Exact = 0.4054651081081644, Error = 3.504664114473144e-09
24 terms: Approx = 0.40546510978651285, Exact = 0.4054651081081644, Error = 1.6783484602100884e-09
25 terms: Approx = 0.40546510730298596, Exact = 0.4054651081081644, Error = 8.051784239349047e-10
26 terms: Approx = 0.40546510849507883, Exact = 0.4054651081081644, Error = 3.869144449275552e-10
27 terms: Approx = 0.4054651079219572, Exact = 0.4054651081081644, Error = 1.8620716080164357e-10
28 terms: Approx = 0.40546510819790466, Exact = 0.4054651081081644, Error = 8.974027077002233e-11
29 terms: Approx = 0.4054651080648586, Exact = 0.4054651081081644, Error = 4.3305803387738706e-11
30 terms: Approx = 0.4054651081290877, Exact = 0.4054651081081644, Error = 2.092331863323693e-11
31 terms: Approx = 0.4054651080980436, Exact = 0.4054651081081644, Error = 1.0120793092482927e-11
32 terms: Approx = 0.4054651081130649, Exact = 0.4054651081081644, Error = 4.900524430695441e-12
33 terms: Approx = 0.40546510810578895, Exact = 0.4054651081081644, Error = 2.375433183487985e-12
34 terms: Approx = 0.4054651081093167, Exact = 0.4054651081081644, Error = 1.15230047725845e-12
35 terms: Approx = 0.4054651081076047, Exact = 0.4054651081081644, Error = 5.596634267135414e-13
36 terms: Approx = 0.4054651081084363, Exact = 0.4054651081081644, Error = 2.7189361873070084e-13
37 terms: Approx = 0.40546510810803205, Exact = 0.4054651081081644, Error = 1.3233858453531866e-13
38 terms: Approx = 0.40546510810822867, Exact = 0.4054651081081644, Error = 6.428191312579656e-14
39 terms: Approx = 0.4054651081081329, Exact = 0.4054651081081644, Error = 3.147482274812319e-14
40 terms: Approx = 0.40546510810817954, Exact = 0.4054651081081644, Error = 1.5154544286133387e-14
41 terms: Approx = 0.4054651081081568, Exact = 0.4054651081081644, Error = 7.605027718682322e-15
42 terms: Approx = 0.4054651081081679, Exact = 0.4054651081081644, Error = 3.497202527569243e-15
43 terms: Approx = 0.40546510810816244, Exact = 0.4054651081081644, Error = 1.942890293094024e-15
44 terms: Approx = 0.4054651081081651, Exact = 0.4054651081081644, Error = 7.216449660063518e-16
45 terms: Approx = 0.40546510810816383, Exact = 0.4054651081081644, Error = 5.551115123125783e-16
46 terms: Approx = 0.40546510810816444, Exact = 0.4054651081081644, Error = 5.551115123125783e-17
```

![ln](https://cdn.discordapp.com/attachments/905301278647783428/1090431371396268163/image.png)