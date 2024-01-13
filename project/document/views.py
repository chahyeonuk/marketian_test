from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm
from django.http.response import Http404, HttpResponse


# Create your views here.

def create(request):
    if request.method == 'POST':
        board = BoardForm(request.POST)
        if board.is_valid():
            if request.POST.get('file'):
                board.instance.file = request.POST.get('file')
            board.save()
            return redirect('documents:read')
        else:
            form = BoardForm()
            context = {
                'form': form,
                'err_msg': '생성되지 않았습니다.'
            }
            return render(request, 'document/create.html', context=context)
    
    form = BoardForm()
    context = {
        'form': form
    }
    return render(request, 'document/create.html', context=context)
        


def read(request):
    boards = Board.objects.all()
    context = {
        'board': boards
    }
    return render(request, 'document/read.html', context=context)

def read_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    try:
        # 조회수 1 증가
        board.boardhit = board.boardhit + 1
        board.save()
        context = {
            'board': board
        }
    except Board.DoesNotExist:
        return redirect('documents:read')

    return render(request, 'document/read_detail.html', context=context)

def update(request, pk):
    board = get_object_or_404(Board, pk=pk)
    try:
        if request.method == 'POST':
            board = BoardForm(request.POST, instance=board)
            if board.is_valid():
                if request.POST.get('file'):
                    board.instance.file = request.POST.get('file')
                board.save()
                return redirect('documents:read')
            else:
                form = BoardForm(instance=board)  
                context = {
                    'form': form,
                    'err_msg': '수정이 되지 않았습니다.'
                }
                return render(request, 'document/edit.html', context=context)
        else:
            form = BoardForm(instance=board)
            context = {
                'form': form
            }
    except Board.DoesNotExist as e:
        return redirect('documents:read')
    
    return render(request, 'document/edit.html', context=context)

def delete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    try:
        if request.method == 'POST':
            try:
                board.delete()
                return redirect('documents:read')
            except Exception as e:
                context = {
                    'board': board,
                    'err_msg': '정상적으로 삭제되지 않았습니다.'
                }
                return render(request, 'document/delete.html', context=context)
        else:
            context = {
                'board': board
            }
            return render(request, 'document/delete.html', context=context)
    except Board.DoesNotExist:
        return redirect('documents:read')