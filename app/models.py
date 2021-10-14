from django.db import models

# Create your models here.
class OfficeEquipment(models.Model):
    item_type = models.CharField(max_length=25)
    condition = models.CharField(max_length=25)
    notes = models.TextField(null=True,blank=True)
    borrowed_by = models.EmailField(null=True,blank=True)
    borrowed_since = models.TextField(null =True,blank=True)
    estimated_replacement_cost = models.PositiveIntegerField()
    
def create_office_equipment(item_type,condition,notes,borrowed_by,borrowed_since,estimated_replacement_cost):
    group = OfficeEquipment(item_type=item_type, condition=condition, notes=notes,borrowed_by=borrowed_by,borrowed_since=borrowed_since,estimated_replacement_cost=estimated_replacement_cost)
    group.save()
    return group
    
def all_office_equipment():
    return OfficeEquipment.objects.all()

def all_available_equipment():
    return OfficeEquipment.objects.filter(borrowed_by=False, borrowed_since=False)

def borrowed_objects():
    return OfficeEquipment.objects.filter(borrowed_by="person@office.com")

def find_by_item_type(item_type):
    try:
        return OfficeEquipment.objects.get(item_type=item_type)
    except OfficeEquipment.DoesNotExist:
        None

def find_equipment_by_id(id):
    try:
        return OfficeEquipment.objects.get(id=id)
    except OfficeEquipment.DoesNotExist:
        None

def borrow_office_equipment(id,borrowed_by):
    new = OfficeEquipment.objects.get(id=id)
    new.borrowed_by = borrowed_by
    new.save()

def return_office_equipment(id,borrowed_by):
    new = OfficeEquipment.objects.get(id = id)
    if new.borrowed_by != "":
        new.borrowed_by = borrowed_by
        new.save()
    else:
        None 

def delete_equipment(id):
    new = find_equipment_by_id(id = id)
    new.delete()

   