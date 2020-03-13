# Hello World program in Python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
	res=""
	return render_template('index.html', output=res)

@app.route("/index", methods=["GET", "POST"])
def doIt(): 
	if request.method == "POST":
		s=str(request.form['constructor'])
		s =s.strip()
		comp= str(request.form['name'])
		comp = comp.strip()
		print(s)
		print(comp)
	s1 = """protected sdaTranslateService: SDATranslateService,
			private bannerService: ConflictBannerService,
			protected router: Router,
			public featureSetNavigationService: FeatureSetNavigationService,
			protected saveChangesDialogService: SaveChangesDialogService,
			protected featureSetService: FeatureSetService,
			private exceptionService: ExceptionService,
			private notificationService: UxtNotificationService,
			private defaultMethodService: DefaultMethodService,
			private urlFilterFactory: UrlFilterFactory,
			private windowService: WindowService,
			private viewNativeDataService: ViewNativeDataService,
			private actionMenuProvider: ActionMenuProvider,
			private configService: ConfigService,
			private infomapNavigationService: InfomapNavigationService,
			private iconService: ObjectIconService,
			modalService: ModalService"""

	comp1 = "UpdateReferencesComponent"
	#comp1 = str(request.form['name'])

	x= s.split(",")

	services = []
	for i in range(len(x)):
		services.append(x[i].split(": ")[1])

	#services - list of all the names of the sevices provided in the constructor ex SDATranslateService


	stubs=[]

	#nappend the STub to the service and lowering the first letter
	for service in services:
		stubs.append(service[0].lower()+service[1:]+"Stub")

	stubDeclarations = []

	#stub declaration let serviceStub: any; ==> for all stubs
	for stub in stubs:
		stubDeclarations.append("let "+stub+": any;")

	#stub initializations serviceStub ={};
	stubInit = []
	for stub in stubs:
		stubInit.append(stub+" = {};")

	provides = []

	#for providing the providers ==> provide: service, useValue: serviceStub
	for idx in range(len(services)):
		provides.append("provide: "+services[idx]+", useValue:"+stubs[idx])

	injectors = []

	#for injecting the services available ==> serviceStub = fixture.debugElement.injector.get(service);

	for i in range(len(services)):
		injectors.append(stubs[i]+" = fixture.debugElement.injector.get("+services[i]+");")

	directory = "const dirName: string = \"\";"
	fixture = "let fixture: ComponentFixture<"+comp+">;"
	compDec= "let comp: "+comp+";"

	res=""

	res+="describe("+comp+"\",() =>{\n\t"+fixture+"\n\t"+compDec+"\n"

	for stub in stubDeclarations:
		res+="\n\t"+stub

	res+="\n"

	res+="\n\t"+"beforeEach(async(() => {"

	res+="\n\t\t"+directory+"\n"

	for stub in stubInit:
		res+="\n\t\t"+stub

	res+="\n"

	matchers = "jasmine.addMatchers(asyncCustomMatchers);"
	TestBed = "TestBed.configureTestingModule({\n\t\t\timports:[]\n\t\t});"

	res+="\n\t\t"+matchers+"\n\t\t"+TestBed

	res+="\n\t\t"+"TestBed.overrideComponent("+comp+", {\n\t\t\t"+"set: {"+"\n\t\t\t\tproviders: ["
	for pro in provides:
		res+="\n\t\t\t\t\t{ "+pro+" },"

	res+="\n\t\t\t\t]\n\t\t\t}\n\t\t});"
	res+="\n\t\tTestBed.compileComponents();"
	res+="\n\t}));"

	res+="\n\tbeforeEach(() => {"
	res+="\n\t\tfixture = TestBed.createComponent("+comp+");"
	res+="\n\t\tcomp = fixture.componentInstance;"
	res+="\n"

	for inj in injectors:
		res+="\n\t\t"+inj

	res+="\n\t});"
	res+="\n});"
	#print(res)
	#return res
	return render_template('index.html', output=res)
    

if __name__ == "__main__":
	app.run(debug=True)
