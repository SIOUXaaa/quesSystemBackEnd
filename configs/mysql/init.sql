create table question
(
    question_id varchar(255) not null
        primary key,
    user_id     varchar(255) not null,
    answer      json         not null,
    time        timestamp    not null,
    ip          varchar(255) not null
);

create index question_question_id_index
    on question (question_id);

