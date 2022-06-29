from fastapi import Request, Form

from models.base import User


async def home(req: Request, id: int):

    return req.app.state.views.TemplateResponse("index.html", {"request": req, "id": id})
    # return request.state.views.get_template("index.html").render({"request": request, "id": id})


async def reg_page(req: Request):
    return req.app.state.views.TemplateResponse("reg_page.html", {"request": req})


async def reg_result_page(req: Request, username: str = Form(...), password: str = Form(...)):

    user_list = await User().all().values()
    for user in user_list:
          print(f"用户：{user.get('username')}", user)
        
  
    add_user = await User.create(username=username, password=password)
    print("插入的自增id", add_user.pk)
    print("插入的自增用户民", add_user.username)
    get_user = await User().get_or_none(username=username)
    if not get_user:
        print("")
        return {"info":"没有查询到用户"}
    return req.app.state.views.TemplateResponse("reg_result.html", {"request": req, "username": get_user.username, "password": get_user.password})
