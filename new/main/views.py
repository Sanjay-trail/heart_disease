from django.shortcuts import render
from .ML import cardiom
from .forms import MyForm


# Create your views here.
def explore(request):

	return render(request,'explore.html')
def homepage(request):
	result=cardiom.acc()
	if result>0.5:
		result=" Report:\n  You have been diagonised with the possiblity of having Cardiomyopathy"
	else:
		result="Report: \n You are not diagonised with any disease"

	return render(request, 'display.html',{'result': result})

def prediction(request):
	if request.method == 'POST':
		form = MyForm(request.POST, request.FILES)
		if form.is_valid():
			uploaded_file = request.FILES.get('varient')
			file=request.FILES.get('bt')

	result=cardiom.accu(uploaded_file)
	if result>0.5:
		result=" Report:\n  You have been diagonised with the possiblity of having Cardiomyopathy"
	else:
		result="Report: \n You are not diagonised with any disease"

	gene=file.varient()
	val=""
	if gene =="no":
		gene="no"
		val="There is no gene varient or presence of any disease causing genes"   #if error , write it in seperate functions 
	else:
		val="The gene "+gene+"is present in the given report "
		return render(request,'')
	return render(request, 'display.html', {'result': result},{'gene':gene},{'val':val})
	'''else:
	form = MyForm()

	return  render(request, 'index.html', {'form': form})'''
'''
def display(request):
    gene=file.varient()
	if gene =="none":
		gene="no"
		return render(request,'')'''


# have to replicate simmilar functions for other ML predictions

