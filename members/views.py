from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm

def list_members(request):
    members = Member.objects.all()
    return render(request, 'members/list.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_members')
        else:
            # Form is not valid, re-render the form with errors
            return render(request, 'members/add.html', {'form': form})
    else:
        form = MemberForm()
    return render(request, 'members/add.html', {'form': form})

def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('list_members')
        else:
            # Form is not valid, re-render the form with errors
            return render(request, 'members/edit.html', {'form': form, 'member': member})
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/edit.html', {'form': form, 'member': member})

def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('list_members')
    return render(request, 'members/confirm_delete.html', {'member': member})
