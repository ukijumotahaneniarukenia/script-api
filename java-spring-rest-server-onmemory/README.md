# java-spring-rest-server-onmemory

テーブルなどの作成は事前にする必要がなく、ドメインファーストでらくできた

- https://start.spring.io/

mavenタスクのプラグインのスプリングブートランを起動

8080ポートで起動

GET

```
$ curl -X GET -s http://localhost:8080/employees | jq
{
  "_embedded": {
    "employeeList": [
      {
        "id": 1,
        "name": "Bilbo Baggins",
        "role": "burglar",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/1"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 2,
        "name": "Frodo Baggins",
        "role": "thief",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/2"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "http://localhost:8080/employees"
    }
  }
}
```


POST

```
$ curl -X POST -H 'Content-Type:application/json' -s http://localhost:8080/employees -d '{"id":3,"name":"まりこ","role":"Chef"}'
{"id":3,"name":"まりこ","role":"Chef"}

$ curl -X GET -s http://localhost:8080/employees | jq
{
  "_embedded": {
    "employeeList": [
      {
        "id": 1,
        "name": "Bilbo Baggins",
        "role": "burglar",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/1"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 2,
        "name": "Frodo Baggins",
        "role": "thief",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/2"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 3,
        "name": "まりこ",
        "role": "Chef",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/3"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "http://localhost:8080/employees"
    }
  }
}

```


PUT

```
$ curl -X PUT -H 'Content-Type:application/json' -s http://localhost:8080/employees/3 -d '{"name":"ぽるこ","role":"ぶた"}'
{"id":3,"name":"ぽるこ","role":"ぶた"}

$ curl -X GET -s http://localhost:8080/employees | jq
{
  "_embedded": {
    "employeeList": [
      {
        "id": 1,
        "name": "Bilbo Baggins",
        "role": "burglar",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/1"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 2,
        "name": "Frodo Baggins",
        "role": "thief",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/2"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 3,
        "name": "ぽるこ",
        "role": "ぶた",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/3"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "http://localhost:8080/employees"
    }
  }
}
```


DELETE

```
$ curl -X DELETE -H 'Content-Type:application/json' -s http://localhost:8080/employees/3

$ curl -X GET -s http://localhost:8080/employees | jq
{
  "_embedded": {
    "employeeList": [
      {
        "id": 1,
        "name": "Bilbo Baggins",
        "role": "burglar",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/1"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 2,
        "name": "Frodo Baggins",
        "role": "thief",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/2"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "http://localhost:8080/employees"
    }
  }
}
```


単一のポータブルな実行可能なjarファイルの作成

```
$ cd /home/aine/java-rest-server-onmemory/payroll


$ ./mvnw package
[INFO] Scanning for projects...
[INFO] 
[INFO] ----------------------------< app:payroll >-----------------------------
[INFO] Building payroll 0.0.1-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- maven-resources-plugin:3.1.0:resources (default-resources) @ payroll ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] Copying 1 resource
[INFO] Copying 0 resource
[INFO] 
[INFO] --- maven-compiler-plugin:3.8.1:compile (default-compile) @ payroll ---
[INFO] Nothing to compile - all classes are up to date
[INFO] 
[INFO] --- maven-resources-plugin:3.1.0:testResources (default-testResources) @ payroll ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] skip non existing resourceDirectory /home/aine/java-rest-server-onmemory/payroll/src/test/resources
[INFO] 
[INFO] --- maven-compiler-plugin:3.8.1:testCompile (default-testCompile) @ payroll ---
[INFO] Nothing to compile - all classes are up to date
[INFO] 
[INFO] --- maven-surefire-plugin:2.22.2:test (default-test) @ payroll ---
[INFO] 
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running payroll.PayrollApplicationTests
22:34:55.529 [main] DEBUG org.springframework.test.context.BootstrapUtils - Instantiating CacheAwareContextLoaderDelegate from class [org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate]
22:34:55.535 [main] DEBUG org.springframework.test.context.BootstrapUtils - Instantiating BootstrapContext using constructor [public org.springframework.test.context.support.DefaultBootstrapContext(java.lang.Class,org.springframework.test.context.CacheAwareContextLoaderDelegate)]
22:34:55.550 [main] DEBUG org.springframework.test.context.BootstrapUtils - Instantiating TestContextBootstrapper for test class [payroll.PayrollApplicationTests] from class [org.springframework.boot.test.context.SpringBootTestContextBootstrapper]
22:34:55.558 [main] INFO org.springframework.boot.test.context.SpringBootTestContextBootstrapper - Neither @ContextConfiguration nor @ContextHierarchy found for test class [payroll.PayrollApplicationTests], using SpringBootContextLoader
22:34:55.560 [main] DEBUG org.springframework.test.context.support.AbstractContextLoader - Did not detect default resource location for test class [payroll.PayrollApplicationTests]: class path resource [payroll/PayrollApplicationTests-context.xml] does not exist
22:34:55.561 [main] DEBUG org.springframework.test.context.support.AbstractContextLoader - Did not detect default resource location for test class [payroll.PayrollApplicationTests]: class path resource [payroll/PayrollApplicationTestsContext.groovy] does not exist
22:34:55.561 [main] INFO org.springframework.test.context.support.AbstractContextLoader - Could not detect default resource locations for test class [payroll.PayrollApplicationTests]: no resource found for suffixes {-context.xml, Context.groovy}.
22:34:55.561 [main] INFO org.springframework.test.context.support.AnnotationConfigContextLoaderUtils - Could not detect default configuration classes for test class [payroll.PayrollApplicationTests]: PayrollApplicationTests does not declare any static, non-private, non-final, nested classes annotated with @Configuration.
22:34:55.582 [main] DEBUG org.springframework.test.context.support.ActiveProfilesUtils - Could not find an 'annotation declaring class' for annotation type [org.springframework.test.context.ActiveProfiles] and class [payroll.PayrollApplicationTests]
22:34:55.628 [main] DEBUG org.springframework.context.annotation.ClassPathScanningCandidateComponentProvider - Identified candidate component class: file [/home/aine/java-rest-server-onmemory/payroll/target/classes/payroll/PayrollApplication.class]
22:34:55.629 [main] INFO org.springframework.boot.test.context.SpringBootTestContextBootstrapper - Found @SpringBootConfiguration payroll.PayrollApplication for test class payroll.PayrollApplicationTests
22:34:55.677 [main] DEBUG org.springframework.boot.test.context.SpringBootTestContextBootstrapper - @TestExecutionListeners is not present for class [payroll.PayrollApplicationTests]: using defaults.
22:34:55.677 [main] INFO org.springframework.boot.test.context.SpringBootTestContextBootstrapper - Loaded default TestExecutionListener class names from location [META-INF/spring.factories]: [org.springframework.boot.test.mock.mockito.MockitoTestExecutionListener, org.springframework.boot.test.mock.mockito.ResetMocksTestExecutionListener, org.springframework.boot.test.autoconfigure.restdocs.RestDocsTestExecutionListener, org.springframework.boot.test.autoconfigure.web.client.MockRestServiceServerResetTestExecutionListener, org.springframework.boot.test.autoconfigure.web.servlet.MockMvcPrintOnlyOnFailureTestExecutionListener, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverTestExecutionListener, org.springframework.boot.test.autoconfigure.webservices.client.MockWebServiceServerTestExecutionListener, org.springframework.test.context.web.ServletTestExecutionListener, org.springframework.test.context.support.DirtiesContextBeforeModesTestExecutionListener, org.springframework.test.context.support.DependencyInjectionTestExecutionListener, org.springframework.test.context.support.DirtiesContextTestExecutionListener, org.springframework.test.context.transaction.TransactionalTestExecutionListener, org.springframework.test.context.jdbc.SqlScriptsTestExecutionListener, org.springframework.test.context.event.EventPublishingTestExecutionListener]
22:34:55.686 [main] INFO org.springframework.boot.test.context.SpringBootTestContextBootstrapper - Using TestExecutionListeners: [org.springframework.test.context.web.ServletTestExecutionListener@1b2c4efb, org.springframework.test.context.support.DirtiesContextBeforeModesTestExecutionListener@c35172e, org.springframework.boot.test.mock.mockito.MockitoTestExecutionListener@c2db68f, org.springframework.boot.test.autoconfigure.SpringBootDependencyInjectionTestExecutionListener@3cc41abc, org.springframework.test.context.support.DirtiesContextTestExecutionListener@4566d049, org.springframework.test.context.transaction.TransactionalTestExecutionListener@61ce23ac, org.springframework.test.context.jdbc.SqlScriptsTestExecutionListener@3668d4, org.springframework.test.context.event.EventPublishingTestExecutionListener@1c3b9394, org.springframework.boot.test.mock.mockito.ResetMocksTestExecutionListener@6f2cfcc2, org.springframework.boot.test.autoconfigure.restdocs.RestDocsTestExecutionListener@7f6f61c8, org.springframework.boot.test.autoconfigure.web.client.MockRestServiceServerResetTestExecutionListener@4c2cc639, org.springframework.boot.test.autoconfigure.web.servlet.MockMvcPrintOnlyOnFailureTestExecutionListener@ccb4b1b, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverTestExecutionListener@4097cac, org.springframework.boot.test.autoconfigure.webservices.client.MockWebServiceServerTestExecutionListener@ec2cc4]
22:34:55.688 [main] DEBUG org.springframework.test.context.support.AbstractDirtiesContextTestExecutionListener - Before test class: context [DefaultTestContext@3c9bfddc testClass = PayrollApplicationTests, testInstance = [null], testMethod = [null], testException = [null], mergedContextConfiguration = [WebMergedContextConfiguration@1a9c38eb testClass = PayrollApplicationTests, locations = '{}', classes = '{class payroll.PayrollApplication}', contextInitializerClasses = '[]', activeProfiles = '{}', propertySourceLocations = '{}', propertySourceProperties = '{org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true}', contextCustomizers = set[org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@1c9b0314, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@2d29b4ee, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@4470fbd6, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@0, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizerFactory$Customizer@383dc82c, org.springframework.boot.test.context.SpringBootTestArgs@1], resourceBasePath = 'src/main/webapp', contextLoader = 'org.springframework.boot.test.context.SpringBootContextLoader', parent = [null]], attributes = map['org.springframework.test.context.web.ServletTestExecutionListener.activateListener' -> true]], class annotated with @DirtiesContext [false] with mode [null].
22:34:55.705 [main] DEBUG org.springframework.test.context.support.TestPropertySourceUtils - Adding inlined properties to environment: {spring.jmx.enabled=false, org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true}

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v2.3.3.RELEASE)

2020-08-21 22:34:55.850  INFO 1795892 --- [           main] payroll.PayrollApplicationTests          : Starting PayrollApplicationTests on aine-MS-7B98 with PID 1795892 (started by aine in /home/aine/java-rest-server-onmemory/payroll)
2020-08-21 22:34:55.851  INFO 1795892 --- [           main] payroll.PayrollApplicationTests          : No active profile set, falling back to default profiles: default
2020-08-21 22:34:56.216  INFO 1795892 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Bootstrapping Spring Data JPA repositories in DEFERRED mode.
2020-08-21 22:34:56.249  INFO 1795892 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Finished Spring Data repository scanning in 28ms. Found 1 JPA repository interfaces.
2020-08-21 22:34:56.621  INFO 1795892 --- [           main] o.s.s.concurrent.ThreadPoolTaskExecutor  : Initializing ExecutorService 'applicationTaskExecutor'
2020-08-21 22:34:56.629  INFO 1795892 --- [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Starting...
2020-08-21 22:34:56.748  INFO 1795892 --- [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Start completed.
2020-08-21 22:34:56.801  INFO 1795892 --- [         task-1] o.hibernate.jpa.internal.util.LogHelper  : HHH000204: Processing PersistenceUnitInfo [name: default]
2020-08-21 22:34:56.837  INFO 1795892 --- [         task-1] org.hibernate.Version                    : HHH000412: Hibernate ORM core version 5.4.20.Final
2020-08-21 22:34:56.932  INFO 1795892 --- [         task-1] o.hibernate.annotations.common.Version   : HCANN000001: Hibernate Commons Annotations {5.1.0.Final}
2020-08-21 22:34:56.964  WARN 1795892 --- [           main] JpaBaseConfiguration$JpaWebConfiguration : spring.jpa.open-in-view is enabled by default. Therefore, database queries may be performed during view rendering. Explicitly configure spring.jpa.open-in-view to disable this warning
2020-08-21 22:34:57.027  INFO 1795892 --- [         task-1] org.hibernate.dialect.Dialect            : HHH000400: Using dialect: org.hibernate.dialect.H2Dialect
2020-08-21 22:34:57.366  INFO 1795892 --- [           main] DeferredRepositoryInitializationListener : Triggering deferred initialization of Spring Data repositories…
2020-08-21 22:34:57.392  INFO 1795892 --- [         task-1] o.h.e.t.j.p.i.JtaPlatformInitiator       : HHH000490: Using JtaPlatform implementation: [org.hibernate.engine.transaction.jta.platform.internal.NoJtaPlatform]
2020-08-21 22:34:57.399  INFO 1795892 --- [         task-1] j.LocalContainerEntityManagerFactoryBean : Initialized JPA EntityManagerFactory for persistence unit 'default'
2020-08-21 22:34:57.536  INFO 1795892 --- [           main] DeferredRepositoryInitializationListener : Spring Data repositories initialized!
2020-08-21 22:34:57.541  INFO 1795892 --- [           main] payroll.PayrollApplicationTests          : Started PayrollApplicationTests in 1.83 seconds (JVM running for 2.392)
2020-08-21 22:34:57.576  INFO 1795892 --- [           main] payroll.LoadDatabase                     : Preloading Employee{id=1, name='Bilbo Baggins', role='burglar'}
2020-08-21 22:34:57.578  INFO 1795892 --- [           main] payroll.LoadDatabase                     : Preloading Employee{id=2, name='Frodo Baggins', role='thief'}
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 2.167 s - in payroll.PayrollApplicationTests
2020-08-21 22:34:57.669  INFO 1795892 --- [extShutdownHook] j.LocalContainerEntityManagerFactoryBean : Closing JPA EntityManagerFactory for persistence unit 'default'
2020-08-21 22:34:57.670  INFO 1795892 --- [extShutdownHook] .SchemaDropperImpl$DelayedDropActionImpl : HHH000477: Starting delayed evictData of schema as part of SessionFactory shut-down'
2020-08-21 22:34:57.673  INFO 1795892 --- [extShutdownHook] o.s.s.concurrent.ThreadPoolTaskExecutor  : Shutting down ExecutorService 'applicationTaskExecutor'
2020-08-21 22:34:57.674  INFO 1795892 --- [extShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown initiated...
2020-08-21 22:34:57.676  INFO 1795892 --- [extShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown completed.
[INFO] 
[INFO] Results:
[INFO] 
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0
[INFO] 
[INFO] 
[INFO] --- maven-jar-plugin:3.2.0:jar (default-jar) @ payroll ---
[INFO] Building jar: /home/aine/java-rest-server-onmemory/payroll/target/payroll-0.0.1-SNAPSHOT.jar
[INFO] 
[INFO] --- spring-boot-maven-plugin:2.3.3.RELEASE:repackage (repackage) @ payroll ---
[INFO] Replacing main artifact with repackaged archive
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  3.910 s
[INFO] Finished at: 2020-08-21T22:34:58+09:00
[INFO] ------------------------------------------------------------------------


$ cp /home/aine/java-rest-server-onmemory/payroll/target/payroll-0.0.1-SNAPSHOT.jar /home/aine

$ cd /home/aine

$ java -jar payroll-0.0.1-SNAPSHOT.jar 

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v2.3.3.RELEASE)

2020-08-21 22:32:40.651  INFO 1795722 --- [           main] payroll.PayrollApplication               : Starting PayrollApplication v0.0.1-SNAPSHOT on aine-MS-7B98 with PID 1795722 (/home/aine/payroll-0.0.1-SNAPSHOT.jar started by aine in /home/aine)
2020-08-21 22:32:40.653  INFO 1795722 --- [           main] payroll.PayrollApplication               : No active profile set, falling back to default profiles: default
2020-08-21 22:32:41.099  INFO 1795722 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Bootstrapping Spring Data JPA repositories in DEFERRED mode.
2020-08-21 22:32:41.157  INFO 1795722 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Finished Spring Data repository scanning in 51ms. Found 1 JPA repository interfaces.
2020-08-21 22:32:41.544  INFO 1795722 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8080 (http)
2020-08-21 22:32:41.553  INFO 1795722 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2020-08-21 22:32:41.554  INFO 1795722 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.37]
2020-08-21 22:32:41.599  INFO 1795722 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2020-08-21 22:32:41.599  INFO 1795722 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 906 ms
2020-08-21 22:32:41.745  INFO 1795722 --- [           main] o.s.s.concurrent.ThreadPoolTaskExecutor  : Initializing ExecutorService 'applicationTaskExecutor'
2020-08-21 22:32:41.752  INFO 1795722 --- [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Starting...
2020-08-21 22:32:41.904  INFO 1795722 --- [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Start completed.
2020-08-21 22:32:41.947  INFO 1795722 --- [         task-1] o.hibernate.jpa.internal.util.LogHelper  : HHH000204: Processing PersistenceUnitInfo [name: default]
2020-08-21 22:32:41.981  WARN 1795722 --- [           main] JpaBaseConfiguration$JpaWebConfiguration : spring.jpa.open-in-view is enabled by default. Therefore, database queries may be performed during view rendering. Explicitly configure spring.jpa.open-in-view to disable this warning
2020-08-21 22:32:41.995  INFO 1795722 --- [         task-1] org.hibernate.Version                    : HHH000412: Hibernate ORM core version 5.4.20.Final
2020-08-21 22:32:42.113  INFO 1795722 --- [         task-1] o.hibernate.annotations.common.Version   : HCANN000001: Hibernate Commons Annotations {5.1.0.Final}
2020-08-21 22:32:42.225  INFO 1795722 --- [         task-1] org.hibernate.dialect.Dialect            : HHH000400: Using dialect: org.hibernate.dialect.H2Dialect
2020-08-21 22:32:42.319  INFO 1795722 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
2020-08-21 22:32:42.321  INFO 1795722 --- [           main] DeferredRepositoryInitializationListener : Triggering deferred initialization of Spring Data repositories…
2020-08-21 22:32:42.705  INFO 1795722 --- [         task-1] o.h.e.t.j.p.i.JtaPlatformInitiator       : HHH000490: Using JtaPlatform implementation: [org.hibernate.engine.transaction.jta.platform.internal.NoJtaPlatform]
2020-08-21 22:32:42.710  INFO 1795722 --- [         task-1] j.LocalContainerEntityManagerFactoryBean : Initialized JPA EntityManagerFactory for persistence unit 'default'
2020-08-21 22:32:42.865  INFO 1795722 --- [           main] DeferredRepositoryInitializationListener : Spring Data repositories initialized!
2020-08-21 22:32:42.872  INFO 1795722 --- [           main] payroll.PayrollApplication               : Started PayrollApplication in 2.51 seconds (JVM running for 2.801)
2020-08-21 22:32:42.912  INFO 1795722 --- [           main] payroll.LoadDatabase                     : Preloading Employee{id=1, name='Bilbo Baggins', role='burglar'}
2020-08-21 22:32:42.913  INFO 1795722 --- [           main] payroll.LoadDatabase                     : Preloading Employee{id=2, name='Frodo Baggins', role='thief'}

```

