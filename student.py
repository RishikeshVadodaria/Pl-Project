from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import mysql.connector
from PIL import Image, ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x900")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.configure(bg='#281C2D')

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.va_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # 1st
        img_1 = Image.open("download.jpeg")
        img_1 = img_1.resize((400, 50), Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        self.btn_1 = Button(self.root, cursor="hand2")
        self.btn_1.place(x=0, y=0, width=400, height=50)

        # 2nd
        img_2 = Image.open("download (1).jpeg")
        img_2 = img_2.resize((400, 50), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 = Button(self.root, cursor="hand2")
        self.btn_2.place(x=400, y=0, width=400, height=50)

        # 3rd
        img_3 = Image.open("download (2).jpeg")
        img_3 = img_3.resize((400, 50), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        self.btn_3 = Button(self.root, cursor="hand2")
        self.btn_3.place(x=800, y=0, width=550, height=50)

        # bg
        img_4 = Image.open("download (3).jpeg")
        img_4 = img_4.resize((1200, 600), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        bg_lbl = Label(self.root, image=self.photoimg_4, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=55, width=1350, height=800)
        lbl_title = Label(bg_lbl, text="STUDENT MANGEMENT SYSTEM", font=("times new roman", 37, "bold"), fg="#BEAFC2",
                          bg="#695E93")
        lbl_title.place(x=0, y=0, width=1350, height=50)

        # frames
        Manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="#281C2D")
        Manage_frame.place(x=0, y=60, width=1350, height=600)

        # left

        DataLeftFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student information",
                                   font=("times new roman", 18, "bold"), fg="#341948", bg="#F4B9B8")
        DataLeftFrame.place(x=10, y=10, width=650, height=800)
        img_5 = Image.open("home-page.jpg")
        img_5 = img_5.resize((500, 200), Image.ANTIALIAS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        my_img = Label(DataLeftFrame, image=self.photoimg_5, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=650, height=100)
        # course

        std_lbl_info_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Current Course",
                                        font=("times new roman", 18, "bold"), fg="#341948", bg="#F4B9B8")
        std_lbl_info_frame.place(x=0, y=100, width=640, height=150)

        # Labels and Combo
        # department
        lbl_dep = Label(std_lbl_info_frame, text="Department", font=("arial", 12, "bold"), fg="#341948", bg="#F4B9B8")
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_dep, font=("arial", 12, "bold"), width=17,
                                 state="readonly")
        combo_dep [ "value" ] = ("Select Department", "Computer", "IT", "Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course

        course_std = Label(std_lbl_info_frame, font=("arial", 12, "bold"), text="Courses:", fg="#341948", bg="#F4B9B8")
        course_std.grid(row=0, column=2, sticky=W, padx=2, pady=10)

        com_txtcourse_std = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_course, state="readonly",
                                         font=("arial", 12, "bold"), width=17)

        com_txtcourse_std [ 'value' ] = ("Select Course", "BTI", "B-tech", "Mba", "Mba-tech")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0, column=3, sticky=W, padx=2, pady=10)

        # year
        current_year = Label(std_lbl_info_frame, font=("arial", 12, "bold"), text="Year:", fg="#341948", bg="#F4B9B8")
        current_year.grid(row=1, column=0, sticky=W, padx=2, pady=10)
        com_txt_current_year = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_year, state="readonly",
                                            font=("arial", 12, "bold"), width=17)
        com_txt_current_year [ 'value' ] = ("Select Year", "2020-2021", "2021-2022", "2022-2023", "2023-2024")

        com_txt_current_year.current(0)
        com_txt_current_year.grid(row=1, column=1, sticky=W, padx=2)

        # semster
        label_Semester = Label(std_lbl_info_frame, font=("arial", 12, "bold"), text="Semester:", fg="#341948",
                               bg="#F4B9B8")
        label_Semester.grid(row=1, column=2, sticky=W, padx=2, pady=10)
        comSemester = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_semester, state="readonly",
                                   font=("arial", 12, "bold"), width=17)
        comSemester [ 'value' ] = (
            "Select Semester", "Semster-1", "Semester-2", "Semster-3", "Semester-4", "Semster-5", "Semester-6",
            "Semster-7",
            "Semester-8")
        comSemester.current(0)
        comSemester.grid(row=1, column=3, sticky=W, padx=2, pady=10)
        # Student class Label
        std_lbl_class_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Class Course Details",
                                         font=("times new roman", 18, "bold"), fg="#341948", bg="#F4B9B8")
        std_lbl_class_frame.place(x=0, y=250, width=750, height=600)

        # labels entry

        # ID
        lbl_id = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="StudentID: ", fg="#341948", bg="#F4B9B8")
        lbl_id.grid(row=0, column=0, sticky=W, padx=2, pady=7)
        id_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.va_std_id, font=("arial", 11, "bold"), width=22)
        id_entry.grid(row=0, column=1, sticky=W, padx=2, pady=7)
        # Name

        lbl_Name = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Student Name: ", fg="#341948",
                         bg="#F4B9B8")
        lbl_Name.grid(row=0, column=2, sticky=W, padx=2, pady=7)
        txt_name = ttk.Entry(std_lbl_class_frame, textvariable=self.var_std_name, width=22, font=("arial", 11, "bold"))
        txt_name.grid(row=0, column=3, padx=2, pady=7)

        # Division

        lbl_div = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Class Division:", fg="#341948",
                        bg="#F4B9B8")
        lbl_div.grid(row=1, column=0, sticky=W, padx=2, pady=7)
        com_txt_div = ttk.Combobox(std_lbl_class_frame, textvariable=self.var_div, state="readonly",
                                   font=("arial", 12, "bold"), width=18)
        com_txt_div [ 'value' ] = ("Select Division", "A", "B", "C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # Roll

        lbl_roll = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Roll No: ", fg="#341948", bg="#F4B9B8")
        lbl_roll.grid(row=1, column=2, sticky=W, padx=2, pady=7)
        txt_roll = ttk.Entry(std_lbl_class_frame, textvariable=self.var_roll, width=22, font=("arial", 11, "bold"))
        txt_roll.grid(row=1, column=3, padx=2, pady=7)

        # gender

        lbl_gender = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Gender:", fg="#341948", bg="#F4B9B8")
        lbl_gender.grid(row=2, column=0, sticky=W, padx=2, pady=7)
        com_txt_gender = ttk.Combobox(std_lbl_class_frame, textvariable=self.var_gender, state="readonly",
                                      font=("arial", 12, "bold"), width=18)
        com_txt_gender [ "value" ] = ("Male", "Female", "Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2, column=1, sticky=W, padx=2, pady=7)

        # DOB
        lbl_dob = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="DOB:", fg="#341948", bg="#F4B9B8")
        lbl_dob.grid(row=2, column=2, sticky=W, padx=2, pady=7)
        txt_dob = ttk.Entry(std_lbl_class_frame, textvariable=self.var_dob, width=22, font=("arial", 11, "bold"))
        txt_dob.grid(row=2, column=3, padx=2, pady=7)

        # Email

        lbl_email = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Email:", fg="#341948", bg="#F4B9B8")
        lbl_email.grid(row=3, column=0, sticky=W, padx=2, pady=7)
        txt_email = ttk.Entry(std_lbl_class_frame, textvariable=self.var_email, width=22, font=("arial", 11, "bold"))
        txt_email.grid(row=3, column=1, padx=2, pady=7)

        # phone

        lbl_phone = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Phone No: ", fg="#341948",
                          bg="#F4B9B8")
        lbl_phone.grid(row=3, column=2, sticky=W, padx=2, pady=7)
        txt_phone = ttk.Entry(std_lbl_class_frame, textvariable=self.var_phone, width=22, font=("arial", 11, "bold"))
        txt_phone.grid(row=3, column=3, padx=2, pady=7)

        # Address

        lbl_address = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Address:", fg="#341948",
                            bg="#F4B9B8")
        lbl_address.grid(row=4, column=0, sticky=W, padx=2, pady=7)
        txt_address = ttk.Entry(std_lbl_class_frame, textvariable=self.var_address, width=22,
                                font=("arial", 11, "bold"))
        txt_address.grid(row=4, column=1, padx=2, pady=7)

        # Teacher

        lbl_teacher = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Teacher Name:", fg="#341948",
                            bg="#F4B9B8")
        lbl_teacher.grid(row=4, column=2, sticky=W, padx=2, pady=7)
        txt_teacher = ttk.Entry(std_lbl_class_frame, textvariable=self.var_teacher, width=22,
                                font=("arial", 11, "bold"))
        txt_teacher.grid(row=4, column=3, padx=2, pady=7)

        # Button Frame

        btn_frame = Frame(DataLeftFrame, bd=2, relief=RIDGE, bg="#F4B9B8")
        btn_frame.place(x=0, y=500, width=650, height=38)
        btn_Add = Button(btn_frame, command=self.add_data, text="Save", font=("arial", 11, "bold"), width=16,
                         bg="#323E42", fg="#EFDCF9")
        btn_Add.grid(row=0, column=0, padx=1.5)
        btn_update = Button(btn_frame, command=self.update_data, text="Update", font=("arial", 11, "bold"), width=16,
                            bg="#323E42", fg="#EFDCF9")
        btn_update.grid(row=0, column=1, padx=1.5)
        btn_delete = Button(btn_frame, command=self.delete_data, text="Delete", font=("arial", 11, "bold"), width=16,
                            bg="#323E42", fg="#EFDCF9")
        btn_delete.grid(row=0, column=2, padx=1.5)
        btn_reset = Button(btn_frame, command=self.reset_data, text="Reset", font=("arial", 11, "bold"), width=16,
                           bg="#323E42", fg="#EFDCF9")
        btn_reset.grid(row=0, column=3, padx=1.5)

        #################################################
        # right

        DataRightFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student info",
                                    font=("times new roman", 18, "bold"), fg="#341948", bg="#F4B9B8")
        DataRightFrame.place(x=665, y=10, width=700, height=900)

        # img 1
        img_6 = Image.open(r"college-students-25910347.jpg")
        img_6 = img_6.resize((600, 200), Image.ANTIALIAS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)

        my_img = Label(DataRightFrame, image=self.photoimg_6, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=700, height=200)

        # Search frame
        Search_Frame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, padx=2, text="Search Student information",
                                  font=("times new roman", 18, "bold"), fg="#341948", bg="#F4B9B8")
        Search_Frame.place(x=0, y=200, width=700, height=60)

        search_by = Label(Search_Frame, font=("arial", 11, "bold"), text="Search By", fg="#341948", bg="#BEAFC2")
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        # search
        self.var_com_search = StringVar()

        com_txt_search = ttk.Combobox(Search_Frame, textvariable=self.var_com_search, state="readonly",
                                      font=("arial", 10, "bold"), width=18)
        com_txt_search [ 'value' ] = ("Select Option", "Roll", "Phone", "student_id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=1)

        self.var_search = StringVar()
        txt_search = ttk.Entry(Search_Frame, textvariable=self.var_search, width=15, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(Search_Frame, command=self.search_data(), text="Search", font=("arial", 11, "bold"),
                            width=14,
                            bg="#323E42", fg="#EFDCF9")
        btn_search.grid(row=0, column=3, padx=5)

        btn_ShowAll = Button(Search_Frame, command=self.fetch_data, text="Show All", font=("arial", 11, "bold"),
                             width=14, bg="#323E42", fg="#EFDCF9")
        btn_ShowAll.grid(row=0, column=4, padx=5)

        # ============Student table and scroll bar=============
        table_frame = Frame(DataRightFrame, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=300, width=900, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=(
            "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address",
            "teacher",), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Class Div")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")

        self.student_table [ "show" ] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password='', database="student")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                    self.va_std_id.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(),
                    self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(),
                    self.var_address.get(), self.var_teacher.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student has been added", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}")

        # fetch function

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password='', database="student")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        # Get Cursor

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content [ "values" ]

        self.var_dep.set(data [ 0 ])
        self.var_course.set(data [ 1 ])
        self.var_year.set(data [ 2 ])
        self.var_semester.set(data [ 3 ])
        self.va_std_id.set(data [ 4 ])
        self.var_std_name.set(data [ 5 ])
        self.var_div.set(data [ 6 ])
        self.var_roll.set(data [ 7 ])
        self.var_gender.set(data [ 8 ])
        self.var_dob.set(data [ 9 ])
        self.var_email.set(data [ 10 ])
        self.var_phone.set(data [ 11 ])
        self.var_address.set(data [ 12 ])
        self.var_teacher.set(data [ 13 ])

    def update_data(self):
        if (self.var_dep.get() == "" or self.var_email.get() == "" or self.va_std_id.get() == ""):
            messagebox.showerror("Error", "All Fields are Required")

        else:
            try:
                update = messagebox.askyesno("Update", "Update student's data?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password='', database="student")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep = %s, course = %s, Year = %s, Semester = %s, Name = %s, Division = "
                        "%s, Roll = %s, Gender = %s, Dob = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s "
                        "where student_id = %s",
                        (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                         self.var_std_name.get(), self.var_div.get(), self.var_roll.get(),
                         self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(),
                         self.var_address.get(), self.var_teacher.get(), self.va_std_id.get()))

                else:
                    if not update:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Student's Data Successfully Updated.", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}")

    def delete_data(self):
        if self.va_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)

        else:
            try:
                delete = messagebox.askyesno("Delete", "Delete Student's Data?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password='', database="student")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id = %s"
                    value = (self.va_std_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student's Data has been Deleted.", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")

    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please Select Option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password='', database="student")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()
