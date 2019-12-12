# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MV_Accountingtemplates(models.Model):
    customcolumns = models.CharField(db_column='CustomColumns', max_length=255, blank=True, null=True)
    datatype = models.IntegerField(db_column='DataType', blank=True, null=True)
    filepath = models.CharField(db_column='FilePath', max_length=255, blank=True, null=True)
    includesheaders = models.BooleanField(db_column='IncludesHeaders', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    mvcolumns = models.CharField(db_column='MvColumns', max_length=255, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'AccountingTemplates'


class MV_Activities(models.Model):
    activetime = models.FloatField(db_column='ActiveTime', blank=True, null=True)
    actualenddate = models.DateTimeField(db_column='ActualEndDate', blank=True, null=True)
    actualstartdate = models.DateTimeField(db_column='ActualStartDate', blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    completed = models.BooleanField(db_column='Completed', blank=True, null=True)
    completionpercentageoverride = models.FloatField(db_column='CompletionPercentageOverride', blank=True, null=True)
    duration = models.FloatField(db_column='Duration', blank=True, null=True)
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)
    geolocation = models.CharField(db_column='GeoLocation', max_length=255, blank=True, null=True)
    geolocationend = models.CharField(db_column='GeoLocationEnd', max_length=255, blank=True, null=True)
    ispublicactivity = models.BooleanField(db_column='IsPublicActivity', blank=True, null=True)
    lagdaysoffset = models.FloatField(db_column='LagDaysOffset', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidactivitystation = models.CharField(db_column='LinkIDActivityStation', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkiddepartment = models.CharField(db_column='LinkIDDepartment', max_length=255, blank=True, null=True)
    linkidparent = models.CharField(db_column='LinkIDParent', max_length=255, blank=True, null=True)
    linkidpredecessor = models.CharField(db_column='LinkIDPredecessor', max_length=255, blank=True, null=True)
    linkidproject = models.CharField(db_column='LinkIDProject', max_length=255, blank=True, null=True)
    linkidprojectactivity = models.CharField(db_column='LinkIDProjectActivity', max_length=255, blank=True, null=True)
    linkidshift = models.CharField(db_column='LinkIDShift', max_length=255, blank=True, null=True)
    linkidworkorder = models.CharField(db_column='LinkIDWorkOrder', max_length=255, blank=True, null=True)
    mobile = models.BooleanField(db_column='Mobile', blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    overtime = models.BooleanField(db_column='Overtime', blank=True, null=True)
    predecessorlagdays = models.FloatField(db_column='PredecessorLagDays', blank=True, null=True)
    predecessortype = models.IntegerField(db_column='PredecessorType', blank=True, null=True)
    printflag = models.BooleanField(db_column='PrintFlag', blank=True, null=True)
    scheduledminutes = models.FloatField(db_column='ScheduledMinutes', blank=True, null=True)
    spanproject = models.BooleanField(db_column='SpanProject', blank=True, null=True)
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    startdayofweek = models.IntegerField(db_column='StartDayOfWeek', blank=True, null=True)
    tardyflag = models.BooleanField(db_column='TardyFlag', blank=True, null=True)
    totalminutes = models.FloatField(db_column='TotalMinutes', blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Activities'


class MV_Activitystations(models.Model):
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    laborrate = models.FloatField(db_column='LaborRate', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidparentstation = models.CharField(db_column='LinkIDParentStation', max_length=255, blank=True, null=True)
    linkidprocessingstation = models.CharField(
        db_column='LinkIDProcessingStation', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    numberofemployeesrequired = models.IntegerField(db_column='NumberOfEmployeesRequired', blank=True, null=True)
    stationnumber = models.FloatField(db_column='StationNumber', blank=True, null=True)
    unitsperminutefactorytime = models.FloatField(db_column='UnitsPerMinuteFactoryTime', blank=True, null=True)
    unittype = models.IntegerField(db_column='UnitType', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ActivityStations'


class MV_Attachment(models.Model):
    attachment = models.BinaryField(db_column='Attachment', blank=True, null=True)
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidcreator = models.CharField(db_column='LinkIDCreator', max_length=255, blank=True, null=True)
    linkidparent = models.CharField(db_column='LinkIDParent', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)
    size = models.FloatField(db_column='Size', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Attachment'


class MV_Bundleitemsettings(models.Model):
    bundlebycomment = models.BooleanField(db_column='BundleByComment', blank=True, null=True)
    bundlebyproduct = models.BooleanField(db_column='BundleByProduct', blank=True, null=True)
    bundlebyroom = models.BooleanField(db_column='BundleByRoom', blank=True, null=True)
    bundlebysize = models.BooleanField(db_column='BundleBySize', blank=True, null=True)
    bundlelikeitems = models.BooleanField(db_column='BundleLikeItems', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    maxpiececount = models.IntegerField(db_column='MaxPieceCount', blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'BundleItemSettings'


class MV_Bundleitems(models.Model):
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    depth = models.FloatField(db_column='Depth', blank=True, null=True)
    length = models.FloatField(db_column='Length', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidbundle = models.CharField(db_column='LinkIDBundle', max_length=255, blank=True, null=True)
    linkiditem = models.CharField(db_column='LinkIDItem', max_length=255, blank=True, null=True)
    linkidproduct = models.CharField(db_column='LinkIDProduct', max_length=255, blank=True, null=True)
    linkidproject = models.CharField(db_column='LinkIDProject', max_length=255, blank=True, null=True)
    linkidroom = models.CharField(db_column='LinkIDRoom', max_length=255, blank=True, null=True)
    linkidworkorder = models.CharField(db_column='LinkIDWorkOrder', max_length=255, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)
    scancode = models.CharField(db_column='ScanCode', max_length=255, blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    width = models.FloatField(db_column='Width', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'BundleItems'


class MV_Bundles(models.Model):
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidemployee = models.CharField(db_column='LinkIDEmployee', max_length=255, blank=True, null=True)
    linkidproject = models.CharField(db_column='LinkIDProject', max_length=255, blank=True, null=True)
    linkidstoragegroup = models.CharField(db_column='LinkIDStorageGroup', max_length=255, blank=True, null=True)
    linkidstoragelocation = models.CharField(db_column='LinkIDStorageLocation', max_length=255, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    number = models.CharField(db_column='Number', max_length=255, blank=True, null=True)
    printflag = models.BooleanField(db_column='PrintFlag', blank=True, null=True)
    scancode = models.CharField(db_column='ScanCode', max_length=255, blank=True, null=True)
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Bundles'


class MV_Categories(models.Model):
    categoryfilter = models.IntegerField(db_column='CategoryFilter', blank=True, null=True)
    categorylevel = models.IntegerField(db_column='CategoryLevel', blank=True, null=True)
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidlibrary = models.CharField(db_column='LinkIDLibrary', max_length=255, blank=True, null=True)
    linkidparent = models.CharField(db_column='LinkIDParent', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    visible = models.BooleanField(db_column='Visible', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)
    isexpanded = models.BooleanField(db_column='IsExpanded', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Categories'


class MV_Contacts(models.Model):
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    anniversary = models.DateTimeField(db_column='Anniversary', blank=True, null=True)
    birthday = models.DateTimeField(db_column='Birthday', blank=True, null=True)
    cellphone = models.CharField(db_column='CellPhone', max_length=255, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)
    datefirstcontact = models.DateTimeField(db_column='DateFirstContact', blank=True, null=True)
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)
    emaildefault = models.CharField(db_column='EmailDefault', max_length=255, blank=True, null=True)
    faxdefault = models.CharField(db_column='FaxDefault', max_length=255, blank=True, null=True)
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)
    homephone = models.CharField(db_column='HomePhone', max_length=255, blank=True, null=True)
    jpegname = models.CharField(db_column='JPegName', max_length=255, blank=True, null=True)
    jpegstream = models.BinaryField(db_column='JPegStream', blank=True, null=True)
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidcompany = models.CharField(db_column='LinkIDCompany', max_length=255, blank=True, null=True)
    mailcity = models.CharField(db_column='MailCity', max_length=255, blank=True, null=True)
    mailcountry = models.CharField(db_column='MailCountry', max_length=255, blank=True, null=True)
    mailpobox = models.CharField(db_column='MailPOBox', max_length=255, blank=True, null=True)
    mailstate = models.CharField(db_column='MailState', max_length=255, blank=True, null=True)
    mailstreet = models.CharField(db_column='MailStreet', max_length=255, blank=True, null=True)
    mailzipcode = models.CharField(db_column='MailZipCode', max_length=255, blank=True, null=True)
    managername = models.CharField(db_column='ManagerName', max_length=255, blank=True, null=True)
    middlename = models.CharField(db_column='MiddleName', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    namenickname = models.CharField(db_column='NameNickname', max_length=255, blank=True, null=True)
    namepartner = models.CharField(db_column='NamePartner', max_length=255, blank=True, null=True)
    namesuffix = models.CharField(db_column='NameSuffix', max_length=255, blank=True, null=True)
    office = models.CharField(db_column='Office', max_length=255, blank=True, null=True)
    otheraddressstreet = models.CharField(db_column='OtherAddressStreet', max_length=255, blank=True, null=True)
    phonedefault = models.CharField(db_column='PhoneDefault', max_length=255, blank=True, null=True)
    pobox = models.CharField(db_column='POBox', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    restrictaccess = models.CharField(db_column='RestrictAccess', max_length=255, blank=True, null=True)
    salutation = models.CharField(db_column='Salutation', max_length=255, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)
    tiffname = models.CharField(db_column='TiffName', max_length=255, blank=True, null=True)
    tiffstream = models.BinaryField(db_column='TiffStream', blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)
    websitedefault = models.CharField(db_column='WebSiteDefault', max_length=255, blank=True, null=True)
    wmfname = models.CharField(db_column='WMFName', max_length=255, blank=True, null=True)
    wmfstream = models.BinaryField(db_column='WMFStream', blank=True, null=True)
    zipcode = models.CharField(db_column='ZipCode', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)
    type = models.IntegerField(db_column='Type', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Contacts'


class MV_Departments(models.Model):
    departmentmanager = models.CharField(db_column='DepartmentManager', max_length=255, blank=True, null=True)
    departmentnumber = models.FloatField(db_column='DepartmentNumber', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidprimaryshift = models.CharField(db_column='LinkIDPrimaryShift', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    resourcehours = models.FloatField(db_column='ResourceHours', blank=True, null=True)
    targetnumberofemployees = models.FloatField(db_column='TargetNumberOfEmployees', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Departments'


class MV_Doorlayers(models.Model):
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidlibrary = models.CharField(db_column='LinkIDLibrary', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'DoorLayers'


class MV_Doorwizardfiles(models.Model):
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidlibrary = models.CharField(db_column='LinkIDLibrary', max_length=255, blank=True, null=True)
    linkidproject = models.CharField(db_column='LinkIDProject', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    workbook = models.BinaryField(db_column='WorkBook', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'DoorWizardFiles'


class MV_Edgebandfiles(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'EdgebandFiles'


class MV_Edgebanding(models.Model):
    code = models.CharField(db_column='Code', max_length=255, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    customsizeadjustment = models.FloatField(db_column='CustomSizeAdjustment', blank=True, null=True)
    face = models.IntegerField(db_column='Face', blank=True, null=True)
    grain = models.IntegerField(db_column='Grain', blank=True, null=True)
    hatchtype = models.IntegerField(db_column='HatchType', blank=True, null=True)
    inventoryavailableqty = models.FloatField(db_column='InventoryAvailableQty', blank=True, null=True)
    inventorycurrentqty = models.FloatField(db_column='InventoryCurrentQty', blank=True, null=True)
    inventoryminqty = models.FloatField(db_column='InventoryMinQty', blank=True, null=True)
    linft = models.FloatField(db_column='LinFt', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidbottomfacerendering = models.CharField(
        db_column='LinkIDBottomFaceRendering', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidcorerendering = models.CharField(db_column='LinkIDCoreRendering', max_length=255, blank=True, null=True)
    linkiddefaultvendor = models.CharField(db_column='LinkIDDefaultVendor', max_length=255, blank=True, null=True)
    linkidmaterial = models.CharField(db_column='LinkIDMaterial', max_length=255, blank=True, null=True)
    linkidpart = models.CharField(db_column='LinkIDPart', max_length=255, blank=True, null=True)
    linkidproduct = models.CharField(db_column='LinkIDProduct', max_length=255, blank=True, null=True)
    linkidproject = models.CharField(db_column='LinkIDProject', max_length=255, blank=True, null=True)
    linkidsheetsize = models.CharField(db_column='LinkIDSheetSize', max_length=255, blank=True, null=True)
    linkidsubassembly = models.CharField(db_column='LinkIDSubAssembly', max_length=255, blank=True, null=True)
    linkidtopfacerendering = models.CharField(db_column='LinkIDTopFaceRendering', max_length=255, blank=True, null=True)
    linkidworkorder = models.CharField(db_column='LinkIDWorkOrder', max_length=255, blank=True, null=True)
    markup = models.FloatField(db_column='MarkUp', blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)
    sqft = models.FloatField(db_column='SqFt', blank=True, null=True)
    thickness = models.FloatField(db_column='Thickness', blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    unittype = models.IntegerField(db_column='UnitType', blank=True, null=True)
    vendorcost = models.FloatField(db_column='VendorCost', blank=True, null=True)
    wastefactor = models.FloatField(db_column='WasteFactor', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)
    handlingcode = models.CharField(db_column='HandlingCode', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Edgebanding'


class MV_Employees(models.Model):
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    anniversary = models.DateTimeField(db_column='Anniversary', blank=True, null=True)
    birthday = models.DateTimeField(db_column='Birthday', blank=True, null=True)
    cellphone = models.CharField(db_column='CellPhone', max_length=255, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)
    datefirstcontact = models.DateTimeField(db_column='DateFirstContact', blank=True, null=True)
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)
    department1efficiency = models.FloatField(db_column='Department1Efficiency', blank=True, null=True)
    department1hoursallocation = models.FloatField(db_column='Department1HoursAllocation', blank=True, null=True)
    department2efficiency = models.FloatField(db_column='Department2Efficiency', blank=True, null=True)
    department2hoursallocation = models.FloatField(db_column='Department2HoursAllocation', blank=True, null=True)
    department3efficiency = models.FloatField(db_column='Department3Efficiency', blank=True, null=True)
    department3hoursallocation = models.FloatField(db_column='Department3HoursAllocation', blank=True, null=True)
    emaildefault = models.CharField(db_column='EmailDefault', max_length=255, blank=True, null=True)
    faxdefault = models.CharField(db_column='FaxDefault', max_length=255, blank=True, null=True)
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)
    homephone = models.CharField(db_column='HomePhone', max_length=255, blank=True, null=True)
    jpegname = models.CharField(db_column='JPegName', max_length=255, blank=True, null=True)
    jpegstream = models.BinaryField(db_column='JPegStream', blank=True, null=True)
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidactivitystation = models.CharField(db_column='LinkIDActivityStation', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidcompany = models.CharField(db_column='LinkIDCompany', max_length=255, blank=True, null=True)
    linkidprimarydepartment = models.CharField(
        db_column='LinkIDPrimaryDepartment', max_length=255, blank=True, null=True)
    linkidsecondarydepartment = models.CharField(
        db_column='LinkIDSecondaryDepartment', max_length=255, blank=True, null=True)
    linkidsecondaryshift = models.CharField(db_column='LinkIDSecondaryShift', max_length=255, blank=True, null=True)
    linkidshift = models.CharField(db_column='LinkIDShift', max_length=255, blank=True, null=True)
    linkidtertiarydepartment = models.CharField(
        db_column='LinkIDTertiaryDepartment', max_length=255, blank=True, null=True)
    linkidtertiaryshift = models.CharField(db_column='LinkIDTertiaryShift', max_length=255, blank=True, null=True)
    mailcity = models.CharField(db_column='MailCity', max_length=255, blank=True, null=True)
    mailcountry = models.CharField(db_column='MailCountry', max_length=255, blank=True, null=True)
    mailpobox = models.CharField(db_column='MailPOBox', max_length=255, blank=True, null=True)
    mailstate = models.CharField(db_column='MailState', max_length=255, blank=True, null=True)
    mailstreet = models.CharField(db_column='MailStreet', max_length=255, blank=True, null=True)
    mailzipcode = models.CharField(db_column='MailZipCode', max_length=255, blank=True, null=True)
    managername = models.CharField(db_column='ManagerName', max_length=255, blank=True, null=True)
    middlename = models.CharField(db_column='MiddleName', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    namenickname = models.CharField(db_column='NameNickname', max_length=255, blank=True, null=True)
    namepartner = models.CharField(db_column='NamePartner', max_length=255, blank=True, null=True)
    namesuffix = models.CharField(db_column='NameSuffix', max_length=255, blank=True, null=True)
    office = models.CharField(db_column='Office', max_length=255, blank=True, null=True)
    otheraddressstreet = models.CharField(db_column='OtherAddressStreet', max_length=255, blank=True, null=True)
    phonedefault = models.CharField(db_column='PhoneDefault', max_length=255, blank=True, null=True)
    pobox = models.CharField(db_column='POBox', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    restrictaccess = models.CharField(db_column='RestrictAccess', max_length=255, blank=True, null=True)
    salutation = models.CharField(db_column='Salutation', max_length=255, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)
    tiffname = models.CharField(db_column='TiffName', max_length=255, blank=True, null=True)
    tiffstream = models.BinaryField(db_column='TiffStream', blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)
    websitedefault = models.CharField(db_column='WebSiteDefault', max_length=255, blank=True, null=True)
    wmfname = models.CharField(db_column='WMFName', max_length=255, blank=True, null=True)
    wmfstream = models.BinaryField(db_column='WMFStream', blank=True, null=True)
    zipcode = models.CharField(db_column='ZipCode', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)
    type = models.IntegerField(db_column='Type', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Employees'


class MV_Estimates(models.Model):
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Estimates'



class MV_Factory(models.Model):
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidlibrary = models.CharField(db_column='LinkIDLibrary', max_length=255, blank=True, null=True)
    linkidproject = models.CharField(db_column='LinkIDProject', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    workbook = models.BinaryField(db_column='WorkBook', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Factory'


class MV_Generalcontacts(models.Model):
    cellphone = models.CharField(db_column='CellPhone', max_length=255, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)
    emaildefault = models.CharField(db_column='EmailDefault', max_length=255, blank=True, null=True)
    faxdefault = models.CharField(db_column='FaxDefault', max_length=255, blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidprimarycontact = models.CharField(db_column='LinkIDPrimaryContact', max_length=255, blank=True, null=True)
    mailcity = models.CharField(db_column='MailCity', max_length=255, blank=True, null=True)
    mailcountry = models.CharField(db_column='MailCountry', max_length=255, blank=True, null=True)
    mailpobox = models.CharField(db_column='MailPOBox', max_length=255, blank=True, null=True)
    mailstate = models.CharField(db_column='MailState', max_length=255, blank=True, null=True)
    mailstreet = models.CharField(db_column='MailStreet', max_length=255, blank=True, null=True)
    mailzipcode = models.CharField(db_column='MailZipCode', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    orderprefix = models.CharField(db_column='OrderPrefix', max_length=255, blank=True, null=True)
    phonedefault = models.CharField(db_column='PhoneDefault', max_length=255, blank=True, null=True)
    pobox = models.CharField(db_column='POBox', max_length=255, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)
    websitedefault = models.CharField(db_column='WebSiteDefault', max_length=255, blank=True, null=True)
    zipcode = models.CharField(db_column='ZipCode', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)
    type = models.IntegerField(db_column='Type', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'GeneralContacts'


class MV_Globalfiles(models.Model):
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidlibrary = models.CharField(db_column='LinkIDLibrary', max_length=255, blank=True, null=True)
    linkidproject = models.CharField(db_column='LinkIDProject', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    workbook = models.BinaryField(db_column='WorkBook', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'GlobalFiles'


class MV_Holidays(models.Model):
    datetype = models.IntegerField(db_column='DateType', blank=True, null=True)
    day = models.IntegerField(db_column='Day', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    month = models.IntegerField(db_column='Month', blank=True, null=True)
    moveweekend = models.BooleanField(db_column='MoveWeekend', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    observed = models.BooleanField(db_column='Observed', blank=True, null=True)
    paidholiday = models.BooleanField(db_column='PaidHoliday', blank=True, null=True)
    week = models.IntegerField(db_column='Week', blank=True, null=True)
    weekday = models.IntegerField(db_column='WeekDay', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Holidays'


class MV_Libraries(models.Model):
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidtemplate = models.CharField(db_column='LinkIDTemplate', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Libraries'


class MV_Locations(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Locations'


class MV_Materialcheckout(models.Model):
    checkoutdate = models.DateTimeField(db_column='CheckoutDate', blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidemployee = models.CharField(db_column='LinkIDEmployee', max_length=255, blank=True, null=True)
    linkidreceivedmaterial = models.CharField(db_column='LinkIDReceivedMaterial', max_length=255, blank=True, null=True)
    linkidworkorder = models.CharField(db_column='LinkIDWorkOrder', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'MaterialCheckout'


class MV_Materialcompositions(models.Model):
    code = models.CharField(db_column='Code', max_length=255, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    grain = models.IntegerField(db_column='Grain', blank=True, null=True)
    hatchtype = models.IntegerField(db_column='HatchType', blank=True, null=True)
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidbottomfacerendering = models.CharField(
        db_column='LinkIDBottomFaceRendering', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidcorerendering = models.CharField(db_column='LinkIDCoreRendering', max_length=255, blank=True, null=True)
    linkiddefaultvendor = models.CharField(db_column='LinkIDDefaultVendor', max_length=255, blank=True, null=True)
    linkidmaterialclass = models.CharField(db_column='LinkIDMaterialClass', max_length=255, blank=True, null=True)
    linkidsheetsize = models.CharField(db_column='LinkIDSheetSize', max_length=255, blank=True, null=True)
    linkidtopfacerendering = models.CharField(db_column='LinkIDTopFaceRendering', max_length=255, blank=True, null=True)
    markup = models.FloatField(db_column='MarkUp', blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)
    standardprice = models.FloatField(db_column='StandardPrice', blank=True, null=True)
    thickness = models.FloatField(db_column='Thickness', blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    unittype = models.IntegerField(db_column='UnitType', blank=True, null=True)
    wastefactor = models.FloatField(db_column='WasteFactor', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)
    handlingcode = models.CharField(db_column='HandlingCode', max_length=255, blank=True, null=True)
    codeformula = models.TextField(db_column='CodeFormula', blank=True, null=True)
    grainformula = models.TextField(db_column='GrainFormula', blank=True, null=True)
    handlingcodeformula = models.TextField(db_column='HandlingCodeFormula', blank=True, null=True)
    isformulamaterial = models.BooleanField(db_column='IsFormulaMaterial', blank=True, null=True)
    markupformula = models.TextField(db_column='MarkUpFormula', blank=True, null=True)
    materialcommentsformula = models.TextField(db_column='MaterialCommentsFormula', blank=True, null=True)
    wastefactorformula = models.TextField(db_column='WasteFactorFormula', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'MaterialCompositions'


class MV_Materialcostbreaks(models.Model):
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    defaultestimatecostbreak = models.BooleanField(db_column='DefaultEstimateCostBreak', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidmaterial = models.CharField(db_column='LinkIDMaterial', max_length=255, blank=True, null=True)
    linkidsheet = models.CharField(db_column='LinkIDSheet', max_length=255, blank=True, null=True)
    linkidvendor = models.CharField(db_column='LinkIDVendor', max_length=255, blank=True, null=True)
    maxqty = models.FloatField(db_column='MaxQty', blank=True, null=True)
    minqty = models.FloatField(db_column='MinQty', blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    secondlevelconversion = models.FloatField(db_column='SecondLevelConversion', blank=True, null=True)
    secondlevelunit = models.CharField(db_column='SecondLevelUnit', max_length=255, blank=True, null=True)
    thirdlevelconversion = models.FloatField(db_column='ThirdLevelConversion', blank=True, null=True)
    thirdlevelunit = models.CharField(db_column='ThirdLevelUnit', max_length=255, blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    unitcost = models.FloatField(db_column='UnitCost', blank=True, null=True)
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)
    vendormaterialcode = models.CharField(db_column='VendorMaterialCode', max_length=255, blank=True, null=True)
    waittime = models.FloatField(db_column='WaitTime', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'MaterialCostBreaks'


class MV_Materials(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Materials'


class MV_Partsprocessingstations(models.Model):
    linkidbatch = models.CharField(db_column='LinkIDBatch', max_length=255, blank=True, null=True)
    linkidpart = models.CharField(db_column='LinkIDPart', max_length=255, blank=True, null=True)
    linkidprocessingstation = models.CharField(
        db_column='LinkIDProcessingStation', max_length=255, blank=True, null=True)
    linkidworkorder = models.CharField(db_column='LinkIDWorkOrder', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'PartsProcessingStations'


class MV_Placedsheets(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'PlacedSheets'


class MV_Placedsheetsvendors(models.Model):
    linkidmaterial = models.CharField(db_column='LinkIDMaterial', max_length=255, blank=True, null=True)
    linkidvendor = models.CharField(db_column='LinkIDVendor', max_length=255, blank=True, null=True)
    linkidworkorder = models.CharField(db_column='LinkIDWorkOrder', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'PlacedSheetsVendors'


class MV_Processingstations(models.Model):
    applypartsall = models.BooleanField(db_column='ApplyPartsAll', blank=True, null=True)
    applypartscontainsfacemachining = models.BooleanField(
        db_column='ApplyPartsContainsFaceMachining', blank=True, null=True)
    applypartscontainshboremachining = models.BooleanField(
        db_column='ApplyPartsContainsHboreMachining', blank=True, null=True)
    applypartswithanymachining = models.BooleanField(db_column='ApplyPartsWithAnyMachining', blank=True, null=True)
    applypartswithhboremachining = models.BooleanField(db_column='ApplyPartsWithHBoreMachining', blank=True, null=True)
    applypartswithnomachining = models.BooleanField(db_column='ApplyPartsWithNoMachining', blank=True, null=True)
    folderdestination = models.CharField(db_column='FolderDestination', max_length=255, blank=True, null=True)
    labelimagedestination = models.CharField(db_column='LabelImageDestination', max_length=255, blank=True, null=True)
    labelimagesize = models.IntegerField(db_column='LabelImageSize', blank=True, null=True)
    labelimagetype = models.IntegerField(db_column='LabelImageType', blank=True, null=True)
    labelimagezoom = models.FloatField(db_column='LabelImageZoom', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidnestoptimizationsetting = models.CharField(
        db_column='LinkIDNestOptimizationSetting', max_length=255, blank=True, null=True)
    linkidsawoptimizationsetting = models.CharField(
        db_column='LinkIDSawOptimizationSetting', max_length=255, blank=True, null=True)
    linkidtoolfile = models.CharField(db_column='LinkIDToolFile', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    partpicturesize = models.IntegerField(db_column='PartPictureSize', blank=True, null=True)
    partpicturetype = models.IntegerField(db_column='PartPictureType', blank=True, null=True)
    partpicturezoom = models.FloatField(db_column='PartPictureZoom', blank=True, null=True)
    partsizeadjustmentmode = models.IntegerField(db_column='PartSizeAdjustmentMode', blank=True, null=True)
    scrapminarea = models.FloatField(db_column='ScrapMinArea', blank=True, null=True)
    scrapmindim = models.FloatField(db_column='ScrapMinDim', blank=True, null=True)
    scrapoverridetrims = models.BooleanField(db_column='ScrapOverrideTrims', blank=True, null=True)
    scrapsave = models.BooleanField(db_column='ScrapSave', blank=True, null=True)
    scraptrimleadinglength = models.FloatField(db_column='ScrapTrimLeadingLength', blank=True, null=True)
    scraptrimleadingwidth = models.FloatField(db_column='ScrapTrimLeadingWidth', blank=True, null=True)
    scraptrimtrailinglength = models.FloatField(db_column='ScrapTrimTrailingLength', blank=True, null=True)
    scraptrimtrailingwidth = models.FloatField(db_column='ScrapTrimTrailingWidth', blank=True, null=True)
    scrapuse = models.BooleanField(db_column='ScrapUse', blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    uselegacywmfimagetype = models.BooleanField(db_column='UseLegacyWMFImageType', blank=True, null=True)
    wmffolderdestination = models.CharField(db_column='WMFFolderDestination', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)
    createsubfolders = models.BooleanField(db_column='CreateSubFolders', blank=True, null=True)
    linkidautoloadlistsetting = models.CharField(
        db_column='LinkIDAutoLoadListSetting', max_length=255, blank=True, null=True)
    scrapdimandlogic = models.BooleanField(db_column='ScrapDimAndLogic', blank=True, null=True)
    applypartscontainsface6machining = models.BooleanField(
        db_column='ApplyPartsContainsFace6Machining', blank=True, null=True)
    applypartswithface6machining = models.BooleanField(db_column='ApplyPartsWithFace6Machining', blank=True, null=True)
    linkidbundleitemsetting = models.CharField(
        db_column='LinkIDBundleItemSetting', max_length=255, blank=True, null=True)
    linkidscrapoptimizationsetting = models.CharField(
        db_column='LinkIDScrapOptimizationSetting', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ProcessingStations'


# ANCHOR Projects
class MV_Projects(models.Model):
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkid_category = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    is_inactive = models.BooleanField(db_column='IsInactive', blank=True, null=True)
    total_cost = models.FloatField(db_column='TotalProjectCost', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Projects'


# ANCHOR Products
class MV_Products(models.Model):
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    projects = models.ForeignKey(MV_Projects, db_column='LinkIDProject',
                                 to_field='linkid', null=True, on_delete=models.SET_NULL)
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    depth = models.FloatField(db_column='Depth', blank=True, null=True)
    height = models.FloatField(db_column='Height', blank=True, null=True)
    width = models.FloatField(db_column='Width', blank=True, null=True)
    itemnumber = models.CharField(db_column='ItemNumber', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Products'


class MV_Productsprompts(models.Model):
    linkidproduct = models.CharField(db_column='LinkIDProduct', max_length=255, blank=True, null=True)
    linkidprompt = models.CharField(db_column='LinkIDPrompt', max_length=255, blank=True, null=True)
    linkidsubassembly = models.CharField(db_column='LinkIDSubassembly', max_length=255, blank=True, null=True)
    linkidworkorder = models.CharField(db_column='LinkIDWorkOrder', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ProductsPrompts'


class MV_Projectwizardfiles(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ProjectWizardFiles'


class MV_Projectworkorderactivities(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ProjectWorkOrderActivities'


class MV_Prompts(models.Model):
    controltype = models.IntegerField(db_column='ControlType', blank=True, null=True)
    hideonreports = models.BooleanField(db_column='HideOnReports', blank=True, null=True)
    isquantity = models.BooleanField(db_column='IsQuantity', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidproduct = models.CharField(db_column='LinkIDProduct', max_length=255, blank=True, null=True)
    linkidsubassembly = models.CharField(db_column='LinkIDSubassembly', max_length=255, blank=True, null=True)
    linkidworkorder = models.CharField(db_column='LinkIDWorkOrder', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    value = models.TextField(db_column='Value', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Prompts'


class MV_Purchaseorders(models.Model):
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)
    datedeleted = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)
    expectedarrivaldate = models.DateTimeField(db_column='ExpectedArrivalDate', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkproject = models.CharField(db_column='LinkIDProject', max_length=255, blank=True, null=True)
    linkvendor = models.CharField(db_column='LinkIDVendor', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)


    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'PurchaseOrders'


class MV_Receivedmaterials(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ReceivedMaterials'


class MV_Reporttemplates(models.Model):
    businessobjecttypes = models.IntegerField(db_column='BusinessObjectTypes', blank=True, null=True)
    databasefilename = models.CharField(db_column='DatabaseFileName', max_length=255, blank=True, null=True)
    globalvariables = models.TextField(db_column='GlobalVariables', blank=True, null=True)
    hideinreportlist = models.BooleanField(db_column='HideInReportList', blank=True, null=True)
    isbatchreport = models.BooleanField(db_column='IsBatchReport', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    productvariables = models.TextField(db_column='ProductVariables', blank=True, null=True)
    reportcategorytype = models.IntegerField(db_column='ReportCategoryType', blank=True, null=True)
    reportfile = models.BinaryField(db_column='ReportFile', blank=True, null=True)
    sqlstring = models.CharField(db_column='SqlString', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ReportTemplates'


class MV_Sheetsets(models.Model):
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidproject = models.CharField(db_column='LinkIDProject', max_length=255, blank=True, null=True)
    modelspacefilename = models.CharField(db_column='ModelSpaceFileName', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    paperspacefilename = models.CharField(db_column='PaperSpaceFileName', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'SheetSets'


class MV_Sheets(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Sheets'


class MV_Sheetsvendors(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'SheetsVendors'


class MV_Shifts(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Shifts'


class MV_Shiftsbreaks(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ShiftsBreaks'


class MV_Shiftsholidays(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ShiftsHolidays'


class MV_Shippingitems(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ShippingItems'


class MV_Shippingtickets(models.Model):
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    dateactualdelivery = models.DateTimeField(db_column='DateActualDelivery', blank=True, null=True)
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)
    datedeliveryscheduled = models.DateTimeField(db_column='DateDeliveryScheduled', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidcontactcompany = models.CharField(db_column='LinkIDContactCompany', max_length=255, blank=True, null=True)
    linkidemployeecreator = models.CharField(db_column='LinkIDEmployeeCreator', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    shipmethod = models.IntegerField(db_column='ShipMethod', blank=True, null=True)
    shippingtime = models.IntegerField(db_column='ShippingTime', blank=True, null=True)
    shipstatus = models.IntegerField(db_column='ShipStatus', blank=True, null=True)
    shiptoaddress = models.CharField(db_column='ShipToAddress', max_length=255, blank=True, null=True)
    ticketnumber = models.IntegerField(db_column='TicketNumber', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ShippingTickets'


class MV_Specificationgroups(models.Model):
    categorylevel = models.IntegerField(db_column='CategoryLevel', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidcutpartsfilename = models.CharField(db_column='LinkIDCutPartsFileName', max_length=255, blank=True, null=True)
    linkiddoorwizardfilename = models.CharField(
        db_column='LinkIDDoorWizardFileName', max_length=255, blank=True, null=True)
    linkidedgebandfilename = models.CharField(db_column='LinkIDEdgeBandFileName', max_length=255, blank=True, null=True)
    linkidfactoryfilename = models.CharField(db_column='LinkIDFactoryFileName', max_length=255, blank=True, null=True)
    linkidglobalfilename = models.CharField(db_column='LinkIDGlobalFileName', max_length=255, blank=True, null=True)
    linkidhardwarefilename = models.CharField(db_column='LinkIDHardwareFileName', max_length=255, blank=True, null=True)
    linkidlibrary = models.CharField(db_column='LinkIDLibrary', max_length=255, blank=True, null=True)
    linkidproject = models.CharField(db_column='LinkIDProject', max_length=255, blank=True, null=True)
    linkidprojectwizardfilename = models.CharField(
        db_column='LinkIDProjectWizardFileName', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    printflag = models.BooleanField(db_column='PrintFlag', blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'SpecificationGroups'


class MV_Subassemblies(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Subassemblies'


class MV_Toolfiles(models.Model):

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'ToolFiles'


class MV_Vendors(models.Model):
    accountnumber = models.CharField(db_column='AccountNumber', max_length=255, blank=True, null=True)
    cellphone = models.CharField(db_column='CellPhone', max_length=255, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)
    emaildefault = models.CharField(db_column='EmailDefault', max_length=255, blank=True, null=True)
    faxdefault = models.CharField(db_column='FaxDefault', max_length=255, blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidprimarycontact = models.CharField(db_column='LinkIDPrimaryContact', max_length=255, blank=True, null=True)
    linkidreporttemplate = models.CharField(db_column='LinkIDReportTemplate', max_length=255, blank=True, null=True)
    mailcity = models.CharField(db_column='MailCity', max_length=255, blank=True, null=True)
    mailcountry = models.CharField(db_column='MailCountry', max_length=255, blank=True, null=True)
    mailpobox = models.CharField(db_column='MailPOBox', max_length=255, blank=True, null=True)
    mailstate = models.CharField(db_column='MailState', max_length=255, blank=True, null=True)
    mailstreet = models.CharField(db_column='MailStreet', max_length=255, blank=True, null=True)
    mailzipcode = models.CharField(db_column='MailZipCode', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    paymenttermstype = models.IntegerField(db_column='PaymentTermsType', blank=True, null=True)
    phonedefault = models.CharField(db_column='PhoneDefault', max_length=255, blank=True, null=True)
    pobox = models.CharField(db_column='POBox', max_length=255, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)
    websitedefault = models.CharField(db_column='WebSiteDefault', max_length=255, blank=True, null=True)
    zipcode = models.CharField(db_column='ZipCode', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)
    type = models.IntegerField(db_column='Type', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Vendors'


class MV_Workorderactivities(models.Model):
    actualvalue = models.FloatField(db_column='ActualValue', blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    datestatuschanged = models.DateTimeField(db_column='DateStatusChanged', blank=True, null=True)
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)
    groupingkey = models.CharField(db_column='GroupingKey', max_length=255, blank=True, null=True)
    laborrate = models.FloatField(db_column='LaborRate', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidactivitystation = models.CharField(db_column='LinkIDActivityStation', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    linkidpart = models.CharField(db_column='LinkIDPart', max_length=255, blank=True, null=True)
    linkidproject = models.CharField(db_column='LinkIDProject', max_length=255, blank=True, null=True)
    linkidscheduledactivity = models.CharField(
        db_column='LinkIDScheduledActivity', max_length=255, blank=True, null=True)
    linkidshift = models.CharField(db_column='LinkIDShift', max_length=255, blank=True, null=True)
    linkidstatuschangeemployee = models.CharField(
        db_column='LinkIDStatusChangeEmployee', max_length=255, blank=True, null=True)
    linkidsubassembly = models.CharField(db_column='LinkIDSubassembly', max_length=255, blank=True, null=True)
    linkidworkorder = models.CharField(db_column='LinkIDWorkOrder', max_length=255, blank=True, null=True)
    linkproduct = models.CharField(db_column='LinkProduct', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    numberofemployeesrequired = models.IntegerField(db_column='NumberOfEmployeesRequired', blank=True, null=True)
    priority = models.FloatField(db_column='Priority', blank=True, null=True)
    scheduledvalue = models.FloatField(db_column='ScheduledValue', blank=True, null=True)
    sequencenumber = models.IntegerField(db_column='SequenceNumber', blank=True, null=True)
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    stationnumber = models.FloatField(db_column='StationNumber', blank=True, null=True)
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    totalhours = models.FloatField(db_column='TotalHours', blank=True, null=True)
    totalscheduledvalue = models.FloatField(db_column='TotalScheduledValue', blank=True, null=True)
    type = models.IntegerField(db_column='Type', blank=True, null=True)
    unitsperminutefactorytime = models.FloatField(db_column='UnitsPerMinuteFactoryTime', blank=True, null=True)
    unittype = models.IntegerField(db_column='UnitType', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'WorkOrderActivities'


class MV_WorkOrderBatches(models.Model):
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidworkorder = models.CharField(db_column='LinkIDWorkOrder', max_length=255, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'WorkOrderBatches'


class MV_WorkOrders(models.Model):
    active = models.BooleanField(db_column='Active', blank=True, null=True)
    actualcompletiondate = models.DateTimeField(db_column='ActualCompletionDate', blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)
    estimate = models.BooleanField(db_column='Estimate', blank=True, null=True)
    linkid = models.CharField(db_column='LinkID', max_length=255, blank=True, null=True)
    linkidcategory = models.CharField(db_column='LinkIDCategory', max_length=255, blank=True, null=True)
    modified = models.BooleanField(db_column='Modified', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
    number = models.CharField(db_column='Number', max_length=255, blank=True, null=True)
    scheduledcompletiondate = models.DateTimeField(db_column='ScheduledCompletionDate', blank=True, null=True)
    scheduledstartdate = models.DateTimeField(db_column='ScheduledStartDate', blank=True, null=True)
    shippingtime = models.IntegerField(db_column='ShippingTime', blank=True, null=True)
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    workordernumber = models.IntegerField(db_column='WorkOrderNumber', blank=True, null=True)
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)
    scancode = models.CharField(db_column='ScanCode', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'mv'
        db_table = 'Workorders'
