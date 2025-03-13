--
-- PostgreSQL database dump
--

-- Dumped from database version 16.6
-- Dumped by pg_dump version 16.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: event_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.event_type (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.event_type OWNER TO postgres;

--
-- Name: event_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.event_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.event_type_id_seq OWNER TO postgres;

--
-- Name: event_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.event_type_id_seq OWNED BY public.event_type.id;


--
-- Name: logs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.logs (
    id integer NOT NULL,
    datetime timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    user_id integer NOT NULL,
    event_type_id integer NOT NULL,
    space_type_id integer NOT NULL
);


ALTER TABLE public.logs OWNER TO postgres;

--
-- Name: logs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.logs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.logs_id_seq OWNER TO postgres;

--
-- Name: logs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.logs_id_seq OWNED BY public.logs.id;


--
-- Name: space_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.space_type (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.space_type OWNER TO postgres;

--
-- Name: space_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.space_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.space_type_id_seq OWNER TO postgres;

--
-- Name: space_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.space_type_id_seq OWNED BY public.space_type.id;


--
-- Name: event_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_type ALTER COLUMN id SET DEFAULT nextval('public.event_type_id_seq'::regclass);


--
-- Name: logs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.logs ALTER COLUMN id SET DEFAULT nextval('public.logs_id_seq'::regclass);


--
-- Name: space_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.space_type ALTER COLUMN id SET DEFAULT nextval('public.space_type_id_seq'::regclass);


--
-- Data for Name: event_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.event_type (id, name) FROM stdin;
1	login
2	comment
3	create_post
4	delete_post
5	logout
\.


--
-- Data for Name: logs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.logs (id, datetime, user_id, event_type_id, space_type_id) FROM stdin;
1	2025-03-13 01:35:50.002+10	1	1	1
3	2025-03-14 01:33:50.002+10	2	1	1
4	2025-03-14 01:34:50.002+10	2	2	3
5	2025-03-14 01:36:50.002+10	2	3	2
6	2025-03-14 01:37:50.002+10	2	4	2
7	2025-03-15 01:35:50.002+10	1	1	1
8	2025-03-15 01:36:50.002+10	1	4	2
9	2025-03-15 01:45:50.002+10	1	5	1
10	2025-03-15 01:35:50.002+10	123	1	1
2	2025-03-13 01:36:50.002+10	1	5	1
\.


--
-- Data for Name: space_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.space_type (id, name) FROM stdin;
1	global
2	blog
3	post
\.


--
-- Name: event_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.event_type_id_seq', 5, true);


--
-- Name: logs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.logs_id_seq', 10, true);


--
-- Name: space_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.space_type_id_seq', 3, true);


--
-- Name: event_type event_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_type
    ADD CONSTRAINT event_type_pkey PRIMARY KEY (id);


--
-- Name: logs logs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_pkey PRIMARY KEY (id);


--
-- Name: space_type space_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.space_type
    ADD CONSTRAINT space_type_pkey PRIMARY KEY (id);


--
-- Name: logs logs_event_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_event_type_id_fkey FOREIGN KEY (event_type_id) REFERENCES public.event_type(id) ON DELETE CASCADE;


--
-- Name: logs logs_space_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_space_type_id_fkey FOREIGN KEY (space_type_id) REFERENCES public.space_type(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

