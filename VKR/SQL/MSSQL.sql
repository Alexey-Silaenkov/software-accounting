
CREATE DATABASE Ychpo;

USE Ychpo


CREATE TABLE [DBO].[PO]
(
[id_PO] INT NOT NULL IDENTITY (1,1),
[naim_po] varchar(max) NOT NULL,
[kol_po] int NOT NULL,
[vers_po] varchar(max) NOT NULL,
constraint [PK_id_po] PRIMARY KEY CLUSTERED
	([id_po] ASC) on [PRIMARY],
)

CREATE TABLE [DBO].[role]
(
[id_role] INT NOT NULL IDENTITY (1,1),
[naim_role] varchar(max) NOT NULL,
[polz_role] bit NOT NULL,
[zayavka_role] bit NOT NULL,
[po_role] bit NOT NULL,
[zakaz_role] bit NOT NULL,
constraint [PK_id_role] PRIMARY KEY CLUSTERED
	([id_role] ASC) on [PRIMARY],
)

CREATE TABLE [DBO].[dolj]
(
[id_dolj] INT NOT NULL IDENTITY (1,1),
[naim_dolj] varchar(max) NOT NULL,
[role_id] int null,
constraint [PK_id_dolj] PRIMARY KEY CLUSTERED
	([id_dolj] ASC) on [PRIMARY],
	CONSTRAINT [FK_role_id] FOREIGN KEY ([role_id])
REFERENCES [DBO].[role]([id_role]),
)

CREATE TABLE [DBO].[polz]
(
[id_polz] INT NOT NULL IDENTITY (1,1),
[F_P] varchar(max) NOT NULL,
[I_P] varchar(max) NOT NULL,
[O_P] varchar(max) NULL,
[email] varchar(max) NOT NULL,
[login] varchar(max) NOT NULL,
[password] varchar(max) NOT NULL,
[dostup] bit NOT NULL,
constraint [PK_id_polz] PRIMARY KEY CLUSTERED
	([id_polz] ASC) on [PRIMARY],
)

CREATE TABLE [DBO].[sovm]
(
[id_sovm] INT NOT NULL IDENTITY (1,1),
[polzsovm_id] int Null,
[dolj_id] int null,
constraint [PK_id_sovm] PRIMARY KEY CLUSTERED
	([id_sovm] ASC) on [PRIMARY],
	CONSTRAINT [FK_polzsovm_id] FOREIGN KEY ([polzsovm_id])
REFERENCES [DBO].[polz]([id_polz]) ON DELETE CASCADE,
	CONSTRAINT [FK_dolj_id] FOREIGN KEY ([dolj_id])
REFERENCES [DBO].[dolj]([id_dolj]),
)

CREATE TABLE [DBO].[zayavka]
(
[id_zayavka] INT NOT NULL IDENTITY (1,1),
[status] varchar(max) NOT NULL,
[polz_id] int NOT NULL,
[poz_id] int NOT NULL,
constraint [PK_id_zayavka] PRIMARY KEY CLUSTERED
	([id_zayavka] ASC) on [PRIMARY],
	CONSTRAINT [FK_polz_id] FOREIGN KEY ([polz_id])
REFERENCES [DBO].[polz]([id_polz]) ON DELETE CASCADE,
	CONSTRAINT [FK_poz_id] FOREIGN KEY ([poz_id])
REFERENCES [DBO].[po]([id_po]),
)

CREATE TABLE [DBO].[lickluch]
(
[id_lickluch] INT NOT NULL IDENTITY (1,1),
[kod] varchar(max) NOT NULL,
[statuskluch] bit NOT NULL,
[time] varchar(5) NULL,
[date] varchar(10) NULL,
[pol_id] int NOT NULL,
constraint [PK_id_lickluch] PRIMARY KEY CLUSTERED
	([id_lickluch] ASC) on [PRIMARY],
	CONSTRAINT [FK_pol_id] FOREIGN KEY ([pol_id])
REFERENCES [DBO].[po]([id_po]),
)

CREATE TABLE [DBO].[error]
(
[id_error] INT NOT NULL IDENTITY (1,1),
[naim_error] varchar(max) NOT NULL,
[opisanie] varchar(max) NOT NULL,
[statusError] bit NOT NULL,
[sposobYstranenia] varchar(max) NULL,
constraint [PK_id_error] PRIMARY KEY CLUSTERED
	([id_error] ASC) on [PRIMARY],
)

CREATE TABLE [DBO].[sovmosh]
(
[id_sovmosh] INT NOT NULL IDENTITY (1,1),
[polzsovmosh_id] int Null,
[error_id] int null,
constraint [PK_id_sovmosh] PRIMARY KEY CLUSTERED
	([id_sovmosh] ASC) on [PRIMARY],
	CONSTRAINT [FK_polzsovmosh_id] FOREIGN KEY ([polzsovmosh_id])
REFERENCES [DBO].[polz]([id_polz]) ON DELETE CASCADE,
	CONSTRAINT [FK_error_id] FOREIGN KEY ([error_id])
REFERENCES [DBO].[error]([id_error]),
)
go







create view [dbo].[polzv]
as select id_polz as 'Номер пользователя',F_P as 'Фамилия пользователя', I_P as 'Имя пользователя',O_P as 'Очество пользователя',email as 'Email',login as'Логин', password as'Пароль',id_dolj as 'Номер должности',naim_dolj as 'Должность',id_role as 'Номер роли',naim_role as 'роль', polz_role as 'Доступ к пользователям',zayavka_role as 'Доступ к заявкам',po_role as'Доступ к ПО', zakaz_role as 'Доступ к заказам'
from
polz inner join
sovm on sovm.polzsovm_id=polz.id_polz inner join
dolj on dolj.id_dolj=sovm.dolj_id inner join
role on role.id_role=dolj.role_id
go

create view [dbo].[zahazi]
as select id_zayavka as 'Номер заявки',naim_po as 'Название ПО', vers_po as 'Версия ПО',status as 'Статус',login as 'Логин'
from
zayavka inner join
polz on zayavka.polz_id=polz.id_polz inner join
PO on id_PO=poz_id 
go

create view [dbo].[rols]
as select id_dolj as 'Номер должности',naim_dolj as 'Должность',id_role as 'Номер роли',naim_role as 'роль', polz_role as 'Доступ к пользователям',zayavka_role as 'Доступ к заявкам',po_role as'Доступ к ПО', zakaz_role as 'Доступ к заказам'
from
dolj  inner join
role on role.id_role=dolj.role_id 
go

create view [dbo].[statistika]
as select id_lickluch as 'Номер',naim_po as 'Название ПО', vers_po as 'Версия ПО',F_P as'Фамилия',I_P as 'Имя',O_P as 'Отчество',time as 'Время заказа',date as 'Дата заказа'  from zayavka
join polz on polz.id_polz = zayavka.polz_id
join PO on Po.id_PO = zayavka.poz_id
join lickluch on lickluch.pol_id = PO.id_PO
where lickluch.statuskluch = 1 and zayavka.status = 'Готово'
go

create view [dbo].[izmlickluch]
as select id_lickluch as 'Номер',naim_po as 'Название ПО', kod as 'Код',statuskluch as 'Выдан' from lickluch
join PO on PO.id_PO = lickluch.pol_id
go










CREATE PROCEDURE [DBO].[polz_add]
(
@F_P varchar(max),
@I_P varchar(max),
@O_P varchar(max),
@email varchar(max),
@login varchar(max),
@password varchar(max),
@dostup bit
)
AS
	insert into [dbo].[polz]([F_P],[I_P],[O_P],[email],[login],[password],[dostup]) values((@F_P),(@I_P),(@O_P),(@email),(@login),(@password),(@dostup));
go

CREATE PROCEDURE [DBO].[polz_edit]
@id_polz int,
@F_P varchar(max),
@I_P varchar(max),
@O_P varchar(max),
@email varchar(max),
@login varchar(max)

AS
	update [dbo].polz
	set
	F_P=@F_P,
	I_P=@I_P,
	O_P=@O_P,
	email=@email,
	login=@login

	where id_polz=@id_polz;
go

CREATE PROCEDURE [DBO].[fullpolz_edit]
@id_polz int,
@F_P varchar(max),
@I_P varchar(max),
@O_P varchar(max),
@email varchar(max),
@login varchar(max),
@password varchar(max)

AS
	update [dbo].polz
	set
	F_P=@F_P,
	I_P=@I_P,
	O_P=@O_P,
	email=@email,
	login=@login,
	password=@password

	where id_polz=@id_polz;
go

CREATE PROCEDURE [DBO].[polzpass_edit]
@id_polz int,
@password varchar(max)
AS
	update [dbo].polz
	set
	password=@password
	where id_polz=@id_polz;
go

CREATE PROCEDURE [DBO].[role_add]
(
@naim_role varchar(max),
@polz_role bit,
@zayavka_role bit,
@po_role bit,
@zakaz_role bit
)
AS
	insert into [dbo].[role]([naim_role],[polz_role],[zayavka_role],[po_role],[zakaz_role]) values((@naim_role),(@polz_role),(@zayavka_role),(@po_role),(@zakaz_role));
go

CREATE PROCEDURE [DBO].[dolj_add]
(
@naim_dolj varchar(max),
@role_id int
)
AS
	insert into [dbo].[dolj]([naim_dolj],[role_id]) values((@naim_dolj),(@role_id));
go

CREATE PROCEDURE [DBO].[sovm_add]
(
@polzsovm_id int,
@dolj_id int
)
AS
	insert into [dbo].[sovm]([polzsovm_id],[dolj_id]) values((@polzsovm_id),(@dolj_id));
go

CREATE PROCEDURE [DBO].[sovmosh_add]
(
@polzsovmosh_id int,
@error_id int
)
AS
	insert into [dbo].sovmosh([polzsovmosh_id],[error_id]) values((@polzsovmosh_id),(@error_id));
go

CREATE PROCEDURE [DBO].[zayavka_add]
(
@status varchar(max),
@poz_id int,
@polz_id int
)
AS
	insert into [dbo].[zayavka]([poz_id],[status],[polz_id]) values((@poz_id),(@status),(@polz_id));
go

CREATE PROCEDURE [DBO].[zayavkast_edit]
@id_zayavkast int,
@status varchar(max)
AS
	update [dbo].zayavka
	set
	status=@status
	where id_zayavka=@id_zayavkast;
go

CREATE PROCEDURE [DBO].[lickluchtd_edit]
(
@id_lickluch int,
@time varchar(5),
@date varchar(10),
@statuskluch bit
)
AS
	update [dbo].lickluch
	set
	time=@time,
	date=@date,
	statuskluch=@statuskluch
	where id_lickluch=@id_lickluch;
go

CREATE PROCEDURE [DBO].[po_add]
(
@naim_po varchar(max),
@kol_po int,
@vers_po varchar(max)
)
AS
	insert into [dbo].[po]([naim_po],[kol_po],[vers_po]) values((@naim_po),(@kol_po),(@vers_po));
go

CREATE PROCEDURE [DBO].[po_update]
(
@id_PO int,
@naim_po varchar(max),
@kol_po int,
@vers_po varchar(max)
)
AS
	update [dbo].po
	set
	naim_po=@naim_po,
	kol_po=@kol_po,
	vers_po=@vers_po
	where @id_PO = id_PO
go

CREATE PROCEDURE [DBO].[pokol_update]
(
@id_PO int,
@kol_po int
)
AS
	update [dbo].po
	set
	kol_po=@kol_po
	where @id_PO = id_PO
go

CREATE PROCEDURE [DBO].[po_delete]
@id_po int
AS
	DELETE from dbo.po
	where id_po=@id_po;
go

CREATE PROCEDURE [DBO].[kluch_add]
(
@kod varchar(max),
@statuskluch bit,
@pol_id int
)
AS
	insert into [dbo].[lickluch]([kod],[statuskluch],[pol_id]) values((@kod),(@statuskluch),(@pol_id));
go

CREATE PROCEDURE [DBO].[error_add]
(
@naim_error varchar(max),
@opisanie varchar(max),
@statusError bit,
@sposobYstranenia varchar(max)
)
AS
	insert into [dbo].[error]([naim_error],[opisanie],[statusError],[sposobYstranenia]) values((@naim_error),(@opisanie),(@statusError),(@sposobYstranenia));
go

CREATE PROCEDURE [DBO].[error_update]
(
@id_error int,
@naim_error varchar(max),
@opisanie varchar(max),
@statusError bit,
@sposobYstranenia varchar(max)
)
AS
	update [dbo].error
	set
	naim_error=@naim_error,
	opisanie=@opisanie,
	statusError=@statusError,
	sposobYstranenia=@sposobYstranenia
	where @id_error = id_error
go

CREATE PROCEDURE [DBO].[error_delete]
@id_error int
AS
	DELETE from dbo.error
	where 
	 id_error=@id_error;
go

CREATE PROCEDURE [DBO].[kluch_edit]
@id_lickluch int,
@kod varchar(max)

AS
	update [dbo].lickluch
	set
	kod=@kod

	where id_lickluch=@id_lickluch;
go




