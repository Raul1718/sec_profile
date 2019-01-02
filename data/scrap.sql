CREATE TABLE "secwiki_detail" (
	`ts`	TEXT NOT NULL,
	`tag`	TEXT NOT NULL,
	`url`	TEXT NOT NULL,
	`title`	TEXT,
	`root_domain`	TEXT,
	`domain`	TEXT,
	`path`	TEXT,
	PRIMARY KEY(`ts`,`url`)
);
CREATE TABLE `xuanwu_detail` (
	`ts`	TEXT NOT NULL,
	`tag`	TEXT NOT NULL,
	`url`	TEXT NOT NULL,
	`title`	TEXT,
	`root_domain`	TEXT,
	`domain`	TEXT,
	`path`	TEXT,
	`author_id`	TEXT,
	PRIMARY KEY(`ts`,`url`)
);


/* select substr(ts,1,4) as day,count(distinct url) from secwiki_detail group by day;


2014 2157
2015 2253
2016 2290
2017 4004
2018 3159



select substr(ts,1,4) as day,domain,root_domain,count(distinct url)/2157.0*100 as url_count from secwiki_detail where day = '2014' group by domain order by url_count desc limit 10;
select substr(ts,1,4) as day,domain,root_domain,count(distinct url)/2253.0*100 as url_count from secwiki_detail where day = '2015' group by domain order by url_count desc limit 10;
select substr(ts,1,4) as day,domain,root_domain,count(distinct url)/2290.0*100 as url_count from secwiki_detail where day = '2016' group by domain order by url_count desc limit 10;
select substr(ts,1,4) as day,domain,root_domain,count(distinct url)/4004.0*100 as url_count from secwiki_detail where day = '2017' group by domain order by url_count desc limit 10;
select substr(ts,1,4) as day,domain,root_domain,count(distinct url)/3159.0*100 as url_count from secwiki_detail where day = '2018' group by domain order by url_count desc limit 10;


select substr(ts,1,4) as day,count(distinct url) from xuanwu_detail group by day;
2016|7997
2017|5053
2018|5785

select substr(ts,1,4) as day,domain,root_domain,count(distinct url)/7997.0*100 as url_count from xuanwu_detail where day = '2016' group by domain order by url_count desc limit 10;


select substr(ts,1,4) as day,domain,root_domain,count(distinct url)/5053.0*100 as url_count from xuanwu_detail where day = '2017' group by domain order by url_count desc limit 10;

select substr(ts,1,4) as day,domain,root_domain,count(distinct url)/5785.0*100 as url_count from xuanwu_detail where day = '2018' group by domain order by url_count desc limit 10;



select substr(ts,1,4) as day,tag ,count(distinct url) as url_count from secwiki_detail where day = '2014' group by tag order by url_count desc;
select substr(ts,1,4) as day,tag ,count(distinct url) as url_count from secwiki_detail where day = '2015' group by tag order by url_count desc;
select substr(ts,1,4) as day,tag ,count(distinct url) as url_count from secwiki_detail where day = '2016' group by tag order by url_count desc;
select substr(ts,1,4) as day,tag ,count(distinct url) as url_count from secwiki_detail where day = '2017' group by tag order by url_count desc;
select substr(ts,1,4) as day,tag ,count(distinct url) as url_count from secwiki_detail where day = '2018' group by tag order by url_count desc;


select substr(ts,1,4) as day,tag ,count(distinct url) as url_count from xuanwu_detail where day = '2016' group by tag order by url_count desc;
select substr(ts,1,4) as day,tag ,count(distinct url) as url_count from xuanwu_detail where day = '2017' group by tag order by url_count desc;
select substr(ts,1,4) as day,tag ,count(distinct url) as url_count from xuanwu_detail where day = '2018' group by tag order by url_count desc;

*/