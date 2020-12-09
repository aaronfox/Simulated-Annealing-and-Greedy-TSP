# draw_plots.py draws the results for the final report/slides
import matplotlib.pyplot as plt

temps30 = [2000.0, 3000.0, 4500.0, 6800.0, 10000.0, 15000.0, 22000.0, 33000.0, 22000.0, 15000.0, 10000.0, 6700.0, 4500.0, 3000.0, 2000.0, 1300.0, 870.0, 580.0, 390.0, 260.0, 170.0, 110.0, 73.0, 49.0, 33.0, 22.0, 15.0, 10.0, 6.7, 4.5, 3.0, 33000.0, 30067.686471577297, 27395.93241675977, 24961.58504556526, 22743.548878292993, 20722.60293707598, 18881.234181423857, 17203.48574434791, 15674.818653918257, 14281.985841965015, 13012.917348112422, 11856.615724351313, 10803.060733750566, 9843.122517449085, 8968.482477453992, 8171.5611896339815, 7445.452722218902, 6783.86479062514, 6181.0642300027, 5631.827312981894, 5131.394482085006, 4675.429104524658, 4259.979891967722, 3881.4466596033085, 3536.54912779101, 3222.298495931825, 2935.9715422276727, 2675.0870248840893, 2437.384180254524, 2220.8031315962257, 2023.467038664616, 1843.6658334587476, 1679.8414011756624, 1530.5740779553003, 1394.57034840859, 1270.6516363184187, 1157.7440913763296, 1054.8692834492308, 961.1357237348137, 875.731139330028, 797.9154342658319, 727.0142760102268, 662.4132518617045, 603.5525445938091, 549.9220812111918,
         501.05711277743615, 456.5341870104752, 415.9674787450728, 379.0054464630107, 345.3277859172721, 314.6426544510455, 286.68414195814756, 261.2099665688102, 237.99937509218725, 216.85123002130933, 197.58226652292765, 180.02550430772777, 164.02880061855595, 149.4535317972001, 136.1733920044885, 124.07329868370152, 113.04839528230013, 103.00314258979206, 93.85049081748599, 85.51112524557008, 77.91277890047208, 70.98960630632476, 64.68161288361458, 58.93413505031685, 53.697366520197654, 48.92592669329317, 44.57846739834279, 40.61731457929707, 37.00814182084026, 33.719672883778586, 30.72341067253337, 27.993390286037705, 25.50595401203272, 23.239546314917238, 21.174527040564556, 19.293001219382756, 17.578663992732096, 16.016659318868918, 14.593451233994463, 13.296706552787814, 12.11518799193308, 11.038656790474606, 10.057783983131467, 9.164069557686318, 8.349768795886, 7.607825159541223, 6.931809140232206, 6.315862542706531, 5.754647719141791, 5.243301314349472, 4.7773921210869466, 4.352882680261396, 3.96609429326238, 3.613675143228039, 3.2925712489912953, 3.0000000000000004]

lengths30 = [33702.69724048627, 29877.697636048568, 29122.71088236391, 30412.20100511267, 37238.51477507993, 28178.921222734058, 31449.292932671153, 31317.786040635983, 29641.760321939986, 29745.748846920338, 33034.20836948929, 31854.159023206877, 31909.446685211282, 22995.769469841365, 22041.297570669725, 23339.847413835632, 18425.089835867853, 12977.007327328938, 12436.124579267438, 10871.547362039155, 9845.940577238845, 9238.5940932467, 8955.589153550605, 9043.549845628031, 9040.68900329186, 9014.194062930219, 8964.794027684042, 8987.765124516058, 8955.589153550605, 8955.589153550605, 8955.589153550605, 31667.729360668203, 36548.896104088715, 30280.538662743176, 25740.836345904863, 26818.69442543636, 31314.314479478413, 29414.962373757433, 29048.80767383865, 28028.266530959747, 28409.473643465546, 31337.96580434955, 36108.23123174597, 31854.507332667577, 29361.082619705667, 30579.164790357514, 27898.22902372476, 34732.55608690357, 26584.996943562724, 34779.521344059285, 34111.23468292864, 25454.6422791239, 29944.909068739482, 30005.239954064808, 32104.800318969257, 30969.666230428018, 25836.18150123894, 28762.363396270324, 28572.742081008168, 23449.767041498453, 23470.825418120094, 24679.503319799558, 26549.121535263057, 27875.923841086693, 19383.896459870608,
           25196.143953637733, 24922.14875746156, 21517.0802230997, 19364.483604377543, 19999.78180051887, 23702.53634905461, 21023.11815103812, 21186.616446592656, 14638.654232380755, 16815.52614798632, 20253.162409813194, 15300.264079682505, 16325.142556321998, 13625.166389388447, 12536.149296025835, 13349.599269997725, 12314.540722888805, 11101.077016648234, 10459.226071383286, 11277.62380902211, 11295.215725919583, 11231.577097539379, 10648.871240726696, 10489.201031790764, 9703.320524676967, 9502.229845880738, 10174.435673826303, 9931.517612230857, 9141.628666162169, 9607.43141256809, 10103.619956897954, 9069.645349210421, 9331.773752794541, 9129.054221950719, 9034.993836914957, 8985.758399967743, 8894.684530275117, 9091.465667392516, 9013.695493301531, 8874.615733482911, 9001.526668082055, 8857.255285512072, 8869.962433930126, 8869.962433930126, 8890.031230722332, 8981.457871289851, 8890.031230722332, 8877.324082304278, 8857.255285512072, 8857.255285512072, 8857.255285512072, 8857.255285512072, 8869.962433930126, 8857.255285512072, 8857.255285512072, 8857.255285512072, 8857.255285512072, 8857.255285512072, 8857.255285512072, 8857.255285512072, 8869.962433930126, 8857.255285512072, 8857.255285512072, 8857.255285512072, 8857.255285512072, 8857.255285512072]

acceptances30 = [0.5465, 0.6985, 0.771, 0.856, 0.8975, 0.9345, 0.9525, 0.9685, 0.9825, 0.972, 0.9665, 0.935, 0.896, 0.8585, 0.7745, 0.6635, 0.55, 0.412, 0.2955, 0.198, 0.132, 0.098, 0.0725, 0.053, 0.0455, 0.04, 0.041, 0.035, 0.0335, 0.037, 0.0375, 0.9816666666666667, 0.9808333333333333, 0.9641666666666666, 0.9675, 0.9658333333333333, 0.9733333333333334, 0.9608333333333333, 0.9591666666666666, 0.9616666666666667, 0.9616666666666667, 0.9441666666666667, 0.9408333333333333, 0.9375, 0.925, 0.9216666666666666, 0.9333333333333333, 0.9125, 0.9008333333333334, 0.9175, 0.89, 0.8766666666666667, 0.8625, 0.8608333333333333, 0.835, 0.7983333333333333, 0.8075, 0.7858333333333334, 0.7608333333333334, 0.7433333333333333, 0.71, 0.71, 0.7041666666666667, 0.6333333333333333, 0.6275, 0.5891666666666666, 0.5475, 0.5508333333333333, 0.47333333333333333, 0.49166666666666664, 0.445, 0.42916666666666664, 0.3616666666666667, 0.3958333333333333, 0.3575, 0.2708333333333333, 0.29833333333333334, 0.2525, 0.2475, 0.26, 0.22083333333333333, 0.21, 0.16, 0.16333333333333333, 0.14, 0.13166666666666665, 0.13083333333333333, 0.13666666666666666, 0.12416666666666666, 0.115, 0.09333333333333334, 0.06666666666666667, 0.07833333333333334, 0.07333333333333333, 0.08, 0.0675, 0.07166666666666667, 0.05333333333333334, 0.05, 0.04666666666666667, 0.060833333333333336, 0.05583333333333333, 0.03916666666666667, 0.043333333333333335, 0.041666666666666664, 0.04833333333333333, 0.0325, 0.04, 0.050833333333333335, 0.035833333333333335, 0.03916666666666667, 0.041666666666666664, 0.0575, 0.04, 0.035, 0.035, 0.045, 0.035833333333333335, 0.030833333333333334, 0.034166666666666665, 0.03666666666666667, 0.034166666666666665, 0.0325, 0.029166666666666667, 0.028333333333333332, 0.04, 0.045, 0.0275, 0.03916666666666667, 0.02666666666666667, 0.035833333333333335]

steps = []
for i in range(len(acceptances30) + 1):
    steps.append(i)

plt.title('Temperature vs Step for City Size of 30')
plt.xlabel('Step')
plt.ylabel('Temperature')

plt.plot(steps, temps30)  # , '-o')

plt.show()

plt.draw()
