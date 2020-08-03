import model
import canvas
import analyzer

if __name__=="__main__":
	excelFileName = 'scores.xlsx'
	data, prams = model.makeDataSet(excelFileName)
	analyzer.analysisKmeans(data, prams)
	analyzer.analysisHitNum(data, prams)
	canvas.showPlot()
