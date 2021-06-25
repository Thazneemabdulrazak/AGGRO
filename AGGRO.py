from connection import Db as conn
from flask import Flask, render_template, request, jsonify
from flask.globals import session
import read_csv as rs
app = Flask(__name__)
app.secret_key = 'jj'


@app.route('/')
def hello_world():
    return render_template("LOGIN.html")


@app.route('/addcrop')
def addcrop():
    return render_template("add_crop.html")


@app.route("/b")
def b():
    return render_template("index2.html")


@app.route('/confirmuser', methods=["POST"])
def confirmuser():
    user = request.form["txt_usr"]
    passw = request.form["txt_pswd"]
    a = "select * from login where username='" + user + "' and password='" + passw + "'"
    c = conn()
    print(a)
    r = c.selectone(a)
    print(r)
    if r is None:
        return render_template("LOGIN.html", status="no")
    else:
        if r["type"] == 'admin':
            return render_template("adm_home.html")
        if r["type"]=="user":
            qry="select farmerid from user where Email='"+user+"'"
            dd=c.selectone(qry)
            session["uid"]=dd["farmerid"]
            return render_template("nursery_home.html")
        else:
            return render_template("LOGIN.html", status="no")



@app.route('/usersignup')
def nurserysignup():
    return render_template("nursery_signup.html")


@app.route('/nuhome')
def nuhome():
    return render_template("nursery_home.html")








@app.route('/Home')
def Home():
    return render_template("adm_home.html")


@app.route('/notification')
def Not():
    return render_template("notification.html")


@app.route('/Add_notification', methods=["POST"])
def notification():
    c = conn()
    txt = request.form["txt_not"]
    id=str(session["cid"])
    c = conn()
    n = "update complaint set Reply='"+txt+"',Status='Replied' where Comp_id='"+id+"'"
    print(n)

    c.update(n)
    return viewnotification()
@app.route("/useraddcomplaint")
def useraddcomplatin():
    return render_template("User_add_complain.html")

@app.route('/DeleteNot/<notid>')
def delnot(notid):
    print(str(id))
    f = "delete from notification where Nid='" + notid + "'"
    print(f)

    c = conn()
    c.nonreturn(f)
    return viewnotification()


@app.route('/view_not_table')
def viewnotification():
    s = "select * from user inner join complaint where User_id=farmerid"
    c = conn()
    res = c.select(s)
    return render_template("notification_table.html", res=res)
@app.route("/Reply/<id>/<reply>")
def reply(id,reply):
    session["cid"]=id
    return render_template("notification.html",reply=reply)

@app.route('/View_Crop_table')
def ViewCropTable():
    s = "select * from crop"
    c = conn()
    res = c.select(s)
    return render_template("crop_table.html", res=res)
@app.route('/View_Crop_tableuser')
def View_Crop_tableuser():
    s = "select * from crop"
    c = conn()
    res = c.select(s)
    return render_template("usercrop_table.html", res=res)

@app.route('/DeleteCrp/<id>')
def DeleteCrp(id):
    print(str(id))
    f = "delete from crop where crpid='" + id + "'"
    print(f)

    c = conn()
    c.delete(f)
    return ViewCropTable()


@app.route('/Add_cropinsert', methods=["POST"])
def AC1():
    c = conn()
    nm = request.form["crop_name"]
    des = request.form["crop_des"]

    pic = request.files["crop_file"]
    pic.save("F:\\Riss 2021\\agro\\static\\crop\\" + pic.filename)
    path = "/static/crop/" + pic.filename
    c = conn()
    s = "insert into crop (Photo,Name,Description) values('" + path + "','" + nm + "','" + des + "')"

    c.insert(s)
    return ViewCropTable()















@app.route('/fertiliser')
def Fer():
    return render_template("fertiliser.html")


@app.route('/View_Fertiliser_table')
def ViewFertTable():
    print("HI")
    fe = "select * from fert"
    c = conn()
    res = c.select(fe)
    return render_template("fertiliser_view_det.html", res=res)

@app.route('/View_Fertiliser_tableuser')
def ViewFertTableuser():
    print("HI")
    fe = "select * from fert"
    c = conn()
    res = c.select(fe)
    return render_template("Userfertiliser_view_det.html", res=res)


@app.route('/Add_fertiliser', methods=["POST"])
def Add_fertiliser():
    c = conn()
    nm = request.form["txt_name"]
    photo = request.files["ph"]
    desc = request.form["txt_des"]
    use = request.form["txt_use"]

    print(photo.filename)

    photo.save("F:\\Riss 2021\\agro\\static\\fertiliser\\" + photo.filename)
    path = "/static/fertiliser/" + photo.filename

    c = conn()

    f = "INSERT INTO fert (Name,Photo,fdes,fuse) values ('" + nm + "','" + path + "','" + desc + "','" + use + "')"
    print(f)
    c.insert(f)
    return ViewFertTable()


@app.route('/pesticides')
def Addpesticides():
    return render_template("pesticidenew.html")


@app.route('/Add_pesticide', methods=["POST"])
def pesticide():
    c = conn()
    nm = request.form["txt_name"]
    pho = request.files["fl_name"]
    print("Photo")
    print(pho)
    de = request.form["txt_des"]
    us = request.form["txt_use"]

    pho.save("F:\\Riss 2021\\agro\\static\\pesticide\\" + pho.filename)
    path = "/static/pesticide/" + pho.filename

    p = "INSERT INTO Pesticides (Name,Photo,Details,Puse) values ('" + nm + "','" + path + "','" + de + "','" + us + "')"
    print(p)
    c.insert(p)
    return ViewPesTable()
@app.route('/add_comp', methods=["POST"])
def add_comp():
    c = conn()
    nm = request.form["txt_not"]

    p = "insert into complaint (Complaint,Date,Status,Reply,User_id)values('"+nm+"',curdate(),'pending','pending','"+str(session["uid"])+"')"
    print(p)
    c.insert(p)
    return userviewcomp()

@app.route("/userviewcome")
def userviewcomp():
    pe = "select * from complaint where User_id='"+str(session["uid"])+"'"
    c = conn()
    res = c.select(pe)
    print(res)
    # return "ok"
    return render_template("usernotification_table.html",res=res)

@app.route("/userviewprofile")
def userviewprofile():
    pe = "select * from user where farmerid='"+str(session["uid"])+"'"
    c = conn()
    res = c.selectone(pe)
    print(res)
    # return "ok"
    return render_template("userviewprofile.html",res=res)
@app.route('/View_Pesticides_table')
def ViewPesTable():
    pe = "select * from pesticides"
    c = conn()
    res = c.select(pe)
    print(res)
    # return "ok"
    return render_template("Pesticide_table.html", res=res)
@app.route('/View_Pesticides_tableuser')
def ViewPesTableuser():
    pe = "select * from pesticides"
    c = conn()
    res = c.select(pe)
    print(res)
    # return "ok"
    return render_template("User_Pesticide_table.html", res=res)

@app.route('/viewnursery')
def viewnursery():
    pe = "select * from nursery where status='pending'";
    c = conn()
    res = c.selectall(pe)
    print(res)
    return render_template("nursery.html", res=res)


@app.route('/ViewallPesTable')
def ViewallPesTable():
    pe = "select * from pesticides"
    c = conn()
    res = c.select(pe)
    print(res)

    return render_template("Pesticide_table.html", res=res)


@app.route('/DeleteCrop/<id>')
def delcro(id):
    s = "delete from croptable where crpid='" + id + "'"
    c = conn()
    c.nonreturn(s)
    return ViewCropTable()


@app.route('/DeletePes/<id>')
def delpes(id):
    p = "delete from pesticides where pid='" + id + "'"
    c = conn()
    c.delete(p)
    return ViewPesTable()


@app.route('/DeleteFer/<id>')
def delfer(id):
    print(str(id))
    f = "delete from fert where fid='" + id + "'"
    print(f)

    c = conn()
    c.delete(f)
    return ViewFertTable()


@app.route('/EditCrop/<idc>')
def Editcrop(idc):
    c = conn()
    cr = "Select * from crop where crpid='" + idc + "'"
    w = c.selectone(cr)
    session["cropid"] = idc


    return render_template("edit_crop.html", Photo=w["Photo"], Name=w["Name"], Description=w["Description"])


@app.route('/Newcr', methods=["POST"])
def Newcr():
    c = conn()
    nm1 = request.form["crop_name"]
    de = request.form["crop_des"]


    try:
        df = int(de)
        if type(df)==int:
            return render_template("edit_crop.html",status="in_des")
        else:
            if 'crop_file' not in request.files:
                s = "update crop set Name='" + nm1 + "' , Description='" + de + "' where crpid='" + str(
                    session["cropid"]) + "'"
                print(s)
                re = c.update(s)
                # return ViewPesTable()
                return ViewCropTable()
            else:
                pho = request.files["crop_file"]
                pho.save("F:\\Riss 2021\\agro\\static\\crop\\" + pho.filename)
                path = "/static/crop/" + pho.filename

                s = "update crop set Name='" + nm1 + "' ,Photo='" + path + "', Description='" + de + "'  where crpid='" + str(
                    session["cropid"]) + "'"
                print(s)
                re = c.update(s)
                # return ViewPesTable()
                return ViewCropTable()
    except:
        if 'crop_file' not in request.files:
            s = "update crop set Name='" + nm1 + "' , Description='" + de + "'  where crpid='" + str(
                session["cropid"]) + "'"
            print(s)
            re = c.update(s)
            # return ViewPesTable()
            return ViewCropTable()
        else:
            pho = request.files["crop_file"]
            pho.save("F:\\Riss 2021\\agro\\static\\crop\\" + pho.filename)
            path = "/static/crop/" + pho.filename

            s = "update crop set Name='" + nm1 + "' ,Photo='" + path + "', Description='" + de + "',yt_link='" + yt + "'  where crpid='" + str(
                session["cropid"]) + "'"
            print(s)
            re = c.update(s)
            # return ViewPesTable()
            return ViewCropTable()


@app.route('/Editfert/<idf>')
def Editfert(idf):
    c = conn()
    fr = "Select * from fert where fid='" + idf + "'"
    e = c.selectone(fr)
    session["fertid"] = idf


    return render_template("fertiliser_edit.html", id=e["fid"], name=e["Name"], Photo=e["Photo"], fdes=e["fdes"], fuse=e["fuse"])


@app.route('/Newfe', methods=["POST"])
def Newfe():
    c = conn()
    nm1 = request.form["txt_name"]

    de = request.form["txt_det"]
    us = request.form["txt_use"]
    print("lo")

    if 'fileField' not in request.files:
        print("UI")
        s = "update fert set Name='" + nm1 + "' , fdes='" + de + "', fuse='" + us + "' where fid='" + str(
            session["fertid"]) + "'"
        print(s)
        re = c.update(s)
        print("tre")
        # return ViewPesTable()
        return ViewFertTable()
    else:
        print("qwe")
        pho = request.files["fileField"]
        pho.save("F:\\Riss 2021\\agro\\static\\fertiliser\\" + pho.filename)
        path = "/static/fertiliser/" + pho.filename

        s = "update fert set Name='" + nm1 + "' ,Photo='" + path + "', fdes='" + de + "', fuse='" + us + "' where fid='" + str(session["fertid"]) + "'"
        print(s)
        re = c.update(s)
        print("tyu")        # return ViewPesTable()
        return ViewFertTable()


@app.route('/Editpes/<id>')
def Editpes(id):
    c = conn()
    s = "select * from pesticides where Pid='" + id + "'"
    session["pesid"] = id
    r = c.selectone(s)
    session["id2"] = r["Pid"]
    session["pho4"] = r["Photo"]
    return render_template("pesticide_edit_table.html", name=r["Name"], Photo=r["Photo"], Details=r["Details"], Puse=r["Puse"])


@app.route('/Newpe', methods=["POST"])
def Newpe():
    c = conn()
    nm1 = request.form["txt_name"]
    # pho = request.files["file_photo"]
    de = request.form["txt_des"]
    us = request.form["txt_use"]
    img = ""
    if 'file_photo' not in request.files:
        p = "update pesticides set Name='" + nm1 + "' , Details='" + de + "', Puse='" + us + "' where Pid='" + str(
            session["pesid"]) + "'"
        print(p)
        re = c.update(p)
        # return ViewPesTable()
        return ViewallPesTable()
    else:
        pho = request.files["file_photo"]
        pho.save("F:\\Riss 2021\\agro\\static\\pesticide\\" + pho.filename)
        path = "/static/pesticide/" + pho.filename

        s = "update pesticides set Name='" + nm1 + "' ,Photo='" + path + "', Details='" + de + "', Puse='" + us + "' where Pid='" + str(
            session["pesid"]) + "'"
        print(s)
        re = c.update(s)
        # return ViewPesTable()
        return ViewallPesTable()


@app.route('/logout')
def logout():
    return render_template("LOGIN.html")




@app.route('/farmsignup', methods=['POST'])
def farmrsignup():
    c = conn()
    print ("HLO")
    nam = request.form["name"]
    pl = request.form["place"]
    ci = request.form["city"]
    pi = request.form["pin"]
    pos = request.form["post"]
    email = request.form["email"]
    phone = request.form["phone"]
    pwd = request.form["pass"]
    # sts=request.form["status"]
    print ("REACHED")

    far = "insert into user (Name,Place,City,Pin,Post,Email,Phone) VALUES ('" + nam + "','" + pl + "','" + ci + "','" + pi + "','" + pos + "','" + email + "','" + phone + "')"
    print(far)
    c.insert(far)
    nx = "insert into login (username,password,type) values ('" + email + "','" + pwd + "','user')"
    print(nx)
    re = c.insert(nx);
    print(re)
    return render_template("LOGIN.html")

@app.route('/viewfarmer')
def viewfar():

    fvt="select * from user "
    c=conn()
    qwd = c.select(fvt)
    return render_template("Viewfarmer.html", res=qwd)


@app.route('/user_check')
def user_check():
    return render_template("userdetection.html",my="o")
@app.route('/detect_post', methods=['POST'])
def detect_post():
    temp=request.form["temp"]
    hum=request.form["hum"]
    ph = request.form["ph"]
    rain=request.form["rain"]
    rf,rsc=rs.random_forest(temp,hum,ph,rain)
    svm,ss=rs.mysvm(temp,hum,ph,rain)
    nb,nbs = rs.naive_bayes(temp, hum, ph, rain)
    nn,ns = rs.nn_cnn(float(temp), float(hum), float(ph), float(rain))
    return render_template("userdetection.html",my="oc",rf=rf,temp=temp,hum=hum,ph=ph,rain=rain,svm=svm,nb=nb,
                           nn=nn,ns=ns,rsc=rsc,nbs=nbs)
@app.route('/ff')
def famrloginff():
    return "okkkk"













if __name__ == '__main__':
    app.run(debug=True, port=5000)
