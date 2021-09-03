{{- define "mongodb.namespace" -}}
  {{- if .Values.global -}}
    {{- if .Values.global.namespaceOverride }}
      {{- .Values.global.namespaceOverride -}}
    {{- else -}}
      {{- .Release.Namespace -}}
    {{- end -}}
  {{- else -}}
    {{- .Release.Namespace -}}
  {{- end }}
{{- end -}}

{{- define "mongodb.fullname" -}}
  {{- .Release.Name -}}
{{- end }}

{{- define "mongodb.secretKeyRef" -}}
    {{- if .Values.auth.secretKeyRef -}}
        {{- printf "%s" .Values.auth.secretKeyRef -}}
    {{- else -}}
        {{- printf "%s-secret-key-ref" (include "mongodb.fullname" .) -}}
    {{- end -}}
{{- end -}}

{{- define "mongodb.configMapKeyRef" -}}
    {{- if .Values.auth.configMapKeyRef -}}
        {{- printf "%s" .Values.auth.configMapKeyRef -}}
    {{- else -}}
        {{- printf "%s-cmap-key-ref" (include "mongodb.fullname" .) -}}
    {{- end -}}
{{- end -}}

{{- define "mongodb.meta.name" -}}
  {{ include "mongodb.fullname" . }}-{{ if .Values.useStatefulSet }}sts{{- else }}depl{{- end }}
{{- end -}}

{{- define "mongodb.selector" -}}
  {{- printf "%s-selector" (include "mongodb.fullname" .) -}}
{{- end -}}

{{- define "mongodb.service.name" -}}
  {{- printf "%s-sts-service" (include "mongodb.fullname" .) -}}
{{- end -}}

{{- define "mongodb.secrets" -}}
  {{- printf "%s-secrets" (include "mongodb.fullname" .) -}}
{{- end -}}

{{- define "mongodb.cmap" -}}
  {{- printf "%s-cmap" (include "mongodb.fullname" .) -}}
{{- end -}}

{{- define "mongodb.container" -}}
  {{- printf "%s-container" (include "mongodb.fullname" .) -}}
{{- end -}}

{{- define "mongodb.image" -}}
  {{- printf "%s/%s" .Values.image.registry .Values.image.mongodbImage -}}
{{- end -}}

{{- define "mongodb.net" -}}
  {{- printf "%s-net" (include "mongodb.fullname" .) -}}
{{- end -}}

{{- define "mongo-express.selector" -}}
  {{- printf "%s-express-selector" (include "mongodb.fullname" .) -}}
{{- end -}}

{{- define "mongo-express.container" -}}
  {{- printf "%s-express-container" (include "mongodb.fullname" .) -}}
{{- end -}}

{{- define "mongo-express.net" -}}
  {{- printf "%s-express-net" (include "mongodb.fullname" .) -}}
{{- end -}}

{{- define "mongo-express.image" -}}
  {{- printf "%s/%s" .Values.image.registry .Values.image.mongoExpressImage -}}
{{- end -}}
