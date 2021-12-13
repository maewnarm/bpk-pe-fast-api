-- Clear Trigger
DO $$
DECLARE
    triggNameRecord RECORD;
    triggTableRecord RECORD;
    funcNameRecord RECORD;
	dbName text = 'otsm';
	schemaName text = 'strapi';
BEGIN
    FOR triggNameRecord IN select distinct(trigger_name) from information_schema.triggers where trigger_catalog = dbName and trigger_schema = schemaName LOOP
        FOR triggTableRecord IN SELECT distinct(event_object_table) from information_schema.triggers where trigger_name = triggNameRecord.trigger_name LOOP
            RAISE NOTICE 'Dropping trigger: % on table: %', triggNameRecord.trigger_name, triggTableRecord.event_object_table;
            EXECUTE 'DROP TRIGGER ' || triggNameRecord.trigger_name || ' ON ' || schemaName || '.' || triggTableRecord.event_object_table || ';';
        END LOOP;
    END LOOP;

    FOR funcNameRecord IN select distinct(routine_name) from information_schema.routines where routine_catalog = dbName and routine_schema = schemaName LOOP
        RAISE NOTICE 'Dropping trigger function: % ', funcNameRecord.routine_name;
        EXECUTE 'DROP FUNCTION ' || schemaName || '.' || funcNameRecord.routine_name || '();';
    END LOOP;

END $$;

-- Trigger function
CREATE OR REPLACE FUNCTION strapi.machines_fast_copy()
    RETURNS trigger
    LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
INSERT INTO fast.machines(id,no,name,index,category)
VALUES  (new.id,new.no,new.name,new.index,new.category)
ON CONFLICT (id)
DO
    UPDATE SET no=new.no,name=new.name,index=new.index,category=new.category;
RETURN new;
END;
$BODY$;

ALTER FUNCTION strapi.machines_fast_copy()
    OWNER TO postgres;

CREATE OR REPLACE FUNCTION strapi.machines_fast_delete()
    RETURNS trigger
    LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
DELETE FROM fast.machines
WHERE id=new.id;
RETURN new;
END;
$BODY$;

ALTER FUNCTION strapi.machines_fast_delete()
    OWNER TO postgres;


-- Trigger
CREATE OR REPLACE TRIGGER trigger_machines_fast_copy
    AFTER INSERT OR UPDATE
    ON strapi.machines
    FOR EACH ROW
    EXECUTE FUNCTION strapi.machines_fast_copy();

CREATE OR REPLACE TRIGGER trigger_machine_fast_delete
    AFTER DELETE
    ON strapi.machines
    FOR EACH ROW
    EXECUTE FUNCTION strapi.machines_fast_delete();