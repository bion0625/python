-- 테이블 생성

create table STOCK_PRICE(
    ID varchar(10) primary key,
    STOCK_NAME varchar(20) not null,
    OPEN_PRICE varchar(20) not null,
    CLOSE_PRICE varchar(20) not null,
    HIGH_PRICE varchar(20) not null,
    LOW_PRICE varchar(20) not null,
    CREATED_AT varchar(20) not null,
    UPDATED_AT varchar(20) not null,
    DELETED_AT varchar(20) not null
);